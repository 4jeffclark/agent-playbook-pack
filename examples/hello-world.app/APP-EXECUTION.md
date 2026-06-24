# APP Execution — Hello World

Pack: `hello-world` (reference instance in [`examples/hello-world.app/`](.)).

Framework execution rules: [`../../docs/app-execution.md`](../../docs/app-execution.md). In a distribution repo, the framework text is copied into this file above the pack addendum.

---

## Playbook

| Id | Path |
| --- | --- |
| `hello-world` | `layer3-playbooks/hello-world/` |

## Inputs

| Input | Default | Effect |
| --- | --- | --- |
| `recipient` | `World` | Greeting name |
| `friendly` | `false` | Playbook overlay `friendly-sign-off` |
| `banner` | `false` | Pack overlay `welcome-banner` |

## Sequence

1. `layer0-workflows/input-discovery` → gate `inputs-resolved`
2. `layer1-skills/compose-greeting` (`scripts/run.py`)
3. Overlays when `banner` / `friendly`
4. Outputs under `{userDatastore}/runs/<timestamp>-HelloWorld/` → gate `output-written`

## Contracts

| File | Use |
| --- | --- |
| `contracts/user-datastore-layout.md` | `{userDatastore}` layout |
| `contracts/output-artifact-contract.md` | Report and run manifest |

## Overlays

| Id | Path | When |
| --- | --- | --- |
| `welcome-banner` | `layer2-overlays/welcome-banner.md` | `banner: true` |
| `friendly-sign-off` | `layer3-playbooks/hello-world/overlays/friendly-sign-off.md` | `friendly: true` |
