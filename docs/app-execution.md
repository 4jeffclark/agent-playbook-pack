# APP Execution Guide

Execution contract for APP pack instances. Copied into each `{packId}.app/APP-EXECUTION.md` in distribution repos together with a pack addendum.

Repo shapes and vocabulary: [`../README.md`](../README.md).

---

## Locate the pack

| Context | Path |
| --- | --- |
| Standards Workbench | `examples/{packId}.app/` |
| Distribution repo | `{appRepo}/{packId}.app/` |

Read this file (instance copy), then `pack.app.yaml`, then `README.md`, then the selected `playbook.app.yaml` and manifest-referenced artifacts only.

---

## Execution interface

| Input | Description |
| --- | --- |
| `appRepo` | Path to an APP distribution repo (`README.md` + `*.app/` only) |
| `directive` | Pack and playbook, natural-language intent, or `mode: discovery` |
| `inputs` | Optional partial pack-level and playbook-level parameters |

The executing agent mediates omitted inputs: `userDatastore`, `agentWorkspace`, and remaining manifest inputs.

---

## Instance layout

```text
{packId}.app/
  APP-EXECUTION.md
  pack.app.yaml
  README.md
  layer0-workflows/
  layer1-skills/<id>/SKILL.md
  layer2-overlays/
  layer3-playbooks/<id>/playbook.app.yaml
  contracts/
  gates/
```

Manifests: `pack.app.yaml`, `playbook.app.yaml`. Skills are agentskills.io directories. Workflows, overlays, contracts, and gates are markdown referenced by manifests.

---

## Execution sequence

1. Read `APP-EXECUTION.md`, `pack.app.yaml`, pack `README.md`
2. Resolve directive to a playbook (or stop after discovery)
3. Read `layer3-playbooks/<id>/playbook.app.yaml`
4. Bind `userDatastore` and `agentWorkspace`
5. Run required workflows; clear gates
6. Execute referenced skills per `SKILL.md`
7. Apply overlays when manifest conditions match
8. Write outputs and `run-manifest.yaml` when configured

---

## Data locations

| Role | In APP repo? |
| --- | --- |
| Behavior contract | Yes (read-only) |
| `{userDatastore}` | No — bind at execution |
| `{agentWorkspace}` | No — bind at execution |

Pack-specific layout under `{userDatastore}`: see pack `contracts/`.

---

## Rules

- Prompt-first; run bundled scripts only when `SKILL.md` instructs
- No ad-hoc scripts during a run
- No git required
- Core output runs without optional overlays unless playbook inputs enable them

---

## Version

APP execution guide v0.1.
