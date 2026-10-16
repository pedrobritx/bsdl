import importlib.util
from pathlib import Path
import unittest

SPEC = importlib.util.spec_from_file_location("product_names", Path(__file__).resolve().parents[1] / "automation/check_product_names.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ProductNameTests(unittest.TestCase):
    def test_paths_links_and_case_variants_are_rejected(self):
        for old in MODULE.RETIRED:
            self.assertTrue(MODULE.violations(old + "/constitution.md", b"Polaris"))
            self.assertTrue(MODULE.violations("README.md", ("https://github.com/pedrobritx/" + old.upper()).encode()))

    def test_checksum_substrings_are_not_product_mentions(self):
        for old in MODULE.RETIRED:
            self.assertEqual(MODULE.violations("lock.json", ("abcdef" + old + "123456").encode()), [])

    def test_canonical_names_and_binary_assets_are_allowed(self):
        self.assertEqual(MODULE.violations("polaris/constitution.md", b"Polaris and Axis"), [])
        self.assertEqual(MODULE.violations("asset.png", b"\x89\xff\x00"), [])
