"""CLI regression checks for the bounded documentation validator."""

import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "automation" / "validate_docs.py"
SCRATCH = os.environ.get("VALIDATOR_TEST_SCRATCH")
VALID = """---
title: Example
owner: Engineering
status: Draft
last_updated: 2026-10-15
---

# Example
"""


class ValidatorCLITests(unittest.TestCase):
    def setUp(self):
        if SCRATCH:
            Path(SCRATCH).mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(prefix="fixture-", dir=SCRATCH)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)

    def write(self, relative_path, text):
        path = self.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def run_validator(self, *arguments, script=SCRIPT):
        return subprocess.run(
            [sys.executable, str(script), *arguments],
            cwd=self.root.parent, capture_output=True, text=True, check=False,
        )

    def validate(self):
        return self.run_validator("--root", str(self.root))

    def assert_success(self, result, count=1):
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn(f"{count} documents validated", result.stdout)
        self.assertEqual(result.stderr, "")

    def assert_failure(self, result, message):
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn(message, result.stdout)
        self.assertNotIn("Traceback", result.stdout + result.stderr)

    def test_valid_document(self):
        self.write("docs/example.md", VALID)
        self.assert_success(self.validate())

    def test_default_root_uses_script_location_from_another_working_directory(self):
        copied_script = self.root / "automation" / "validate_docs.py"
        copied_script.parent.mkdir()
        shutil.copyfile(SCRIPT, copied_script)
        self.write("docs/example.md", VALID)
        self.assert_success(self.run_validator(script=copied_script))

    def test_quoted_metadata_and_inline_comments(self):
        self.write("example.md", VALID.replace("title: Example", 'title: "Example #1" # note'))
        self.assert_success(self.validate())

    def test_blank_lines_and_trailing_delimiter_spaces(self):
        self.write("example.md", VALID.replace("---\n", "---  \n").replace("owner:", "\nowner:"))
        self.assert_success(self.validate())

    def test_no_front_matter(self):
        self.write("example.md", "# Example\n")
        self.assert_failure(self.validate(), "missing front matter opening delimiter")

    def test_prefix_is_not_an_opening_delimiter(self):
        self.write("example.md", VALID.replace("---", "---not-a-delimiter", 1))
        self.assert_failure(self.validate(), "missing front matter opening delimiter")

    def test_closing_delimiter_must_be_standalone(self):
        self.write("example.md", VALID.replace("\n---\n", "\n---not-a-delimiter\n"))
        self.assert_failure(self.validate(), "missing front matter closing delimiter")

    def test_missing_closing_delimiter(self):
        self.write("example.md", VALID.replace("\n---\n", "\n"))
        self.assert_failure(self.validate(), "missing front matter closing delimiter")

    def test_required_keys_must_be_top_level_and_exact(self):
        for key in ("title", "owner", "status", "last_updated"):
            for misleading_key in (f"nested_{key}", f"  {key}", f"# {key}"):
                with self.subTest(key=key, misleading_key=misleading_key):
                    self.write("example.md", VALID.replace(f"{key}:", f"{misleading_key}:"))
                    self.assert_failure(self.validate(), f"front matter missing '{key}'")

    def test_required_key_text_inside_another_value_is_not_a_key(self):
        self.write("example.md", VALID.replace("title: Example", 'description: "title: Example"'))
        self.assert_failure(self.validate(), "front matter missing 'title'")

    def test_each_required_value_must_be_nonempty(self):
        values = {"title": "Example", "owner": "Engineering", "status": "Draft", "last_updated": "2026-10-15"}
        for key, value in values.items():
            with self.subTest(key=key):
                self.write("example.md", VALID.replace(f"{key}: {value}", f"{key}:"))
                self.assert_failure(self.validate(), f"front matter '{key}' needs a nonempty scalar value")

    def test_empty_scalar_forms_are_rejected(self):
        for value in ("   ", "# comment", "''", '""', "'  '", "~", "null", "NULL", "[]", "{}", "|", ">-", '"unterminated'):
            with self.subTest(value=value):
                self.write("example.md", VALID.replace("title: Example", f"title: {value}"))
                self.assert_failure(self.validate(), "front matter 'title' needs a nonempty scalar value")

    def test_unquoted_flow_collections_are_rejected(self):
        for value in ("[Example]", "{team: Engineering}", "[ ]", "{ }", "[\t]", "{\t}", "[Example] # comment"):
            with self.subTest(value=value):
                self.write("example.md", VALID.replace("title: Example", f"title: {value}"))
                self.assert_failure(self.validate(), "front matter 'title' needs a nonempty scalar value")

    def test_quoted_collection_text_is_a_valid_scalar(self):
        for value in ("'[Example]'", '"{team: Engineering}"', "'[ ]'", '"{ }"'):
            with self.subTest(value=value):
                self.write("example.md", VALID.replace("title: Example", f"title: {value}"))
                self.assert_success(self.validate())

    def test_keys_in_body_cannot_replace_front_matter_keys(self):
        self.write("example.md", VALID.replace("title: Example\n", "") + "\ntitle: In the body\n")
        self.assert_failure(self.validate(), "front matter missing 'title'")

    def test_existing_relative_file_and_directory_links(self):
        self.write("docs/example.md", VALID + "\n[File](../asset.txt#section) [Directory](../docs)\n")
        self.write("asset.txt", "Existing link target\n")
        self.assert_success(self.validate())

    def test_missing_relative_link_fails(self):
        self.write("docs/example.md", VALID + "\n[Missing](../missing.md#section)\n")
        self.assert_failure(self.validate(), "broken link -> ../missing.md#section")

    def test_existing_external_and_fragment_exemptions(self):
        self.write("example.md", VALID + "\n[Web](https://example.com) [HTTP](http://example.com) [Mail](mailto:a@example.com) [Section](#absent)\n")
        self.assert_success(self.validate())

    def test_unsupported_scheme_retains_existing_relative_link_behavior(self):
        self.write("example.md", VALID + "\n[Call](tel:123)\n")
        self.assert_failure(self.validate(), "broken link -> tel:123")

    def test_root_readme_is_exempt_from_front_matter(self):
        self.write("README.md", "# Public entry point\n")
        self.assert_success(self.validate())

    def test_nested_readme_requires_front_matter(self):
        self.write("docs/README.md", "# Documentation\n")
        self.assert_failure(self.validate(), "missing front matter opening delimiter")

    def test_root_readme_links_are_still_checked(self):
        self.write("README.md", "# Entry point\n[Missing](absent.md)\n")
        self.assert_failure(self.validate(), "broken link -> absent.md")

    def test_github_files_are_exempt_from_front_matter(self):
        self.write(".github/ISSUE_TEMPLATE/bug.md", "# Bug report\n")
        self.assert_success(self.validate())

    def test_github_links_are_still_checked(self):
        self.write(".github/PULL_REQUEST_TEMPLATE.md", "[Missing](../absent.md)\n")
        self.assert_failure(self.validate(), "broken link -> ../absent.md")

    def test_wiki_other_hidden_directories_and_node_modules_remain_ignored(self):
        for directory in (".wiki", ".private", "node_modules", "node_modules-backup"):
            self.write(f"{directory}/ignored.md", "# Invalid\n[Missing](absent.md)\n")
        self.write("example.md", VALID)
        self.assert_success(self.validate())

    def test_invalid_utf8_reports_a_violation(self):
        path = self.write("example.md", VALID)
        path.write_bytes(b"\xff")
        self.assert_failure(self.validate(), "cannot read document")

    def test_invalid_root_is_a_cli_error(self):
        result = self.run_validator("--root", str(self.root / "absent"))
        self.assertEqual(result.returncode, 2)
        self.assertIn("repository root is not a directory", result.stderr)
        self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()
