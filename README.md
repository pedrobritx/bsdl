# Polaris

Governance and orchestration grounded in the Polaris Constitution. The canonical commitments are preserved under [polaris/](polaris/README.md); historical ADRs remain in [decisions/adr/](decisions/adr/).

Polaris owns constitutional commitments, contextual policy adoption, agent delegation and approval/evidence gates. Engineering, design and security capabilities are independently maintained in Axis, Meridian and Sentinel. Full Polaris governance is explicit opt-in, not an implicit consequence of using a capability.

## Start
- [Contributor entry point](AGENTS.md)
- [Operating rules](PROJECT_RULES.md)
- [Capability registry](agents/README.md)
- [Composition, ownership and opt-out contract](integration/README.md)
- [Repository audit and cleanup record](docs/migration/2026-10-16-composition-audit.md)
- [Documentation ownership](https://github.com/pedrobritx/axis/blob/699d2599ab9c69434bfed3a12b1ff226397421fe/docs/README.md)
- [Migration record and gates](docs/migration/2026-10-15-capability-extraction.md)
- [Canonical naming decision](decisions/adr/005-canonical-product-identities.md)
- [File provenance](migration/provenance.json)

## Verification

```sh
python3 automation/validate_docs.py
python3 -m unittest discover -s tests -v
python3 automation/constellation.py --config integration/project.example.json --request integration/request.example.json --workspace ..
```

The planning example requires sibling checkouts for its selected disciplines. Local documentation/tests run without those checkouts. The engineering scaffold is maintained in Axis. Constellation product/application work belongs in its own repository. Canonical philosophical amendments remain separate decisions.
