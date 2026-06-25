# TeamFoundry Stack Realignment

**Program documentation — not APP format.** APP standard: [`../../standard/app-authoring.md`](../../standard/app-authoring.md).

This folder documents the temporary TeamFoundry stack realignment program hosted in the APP Standards Workbench.

## Program layout

```text
documentation/tfy-stack-realignment/
  teamfoundry-stack-realignment-plan.md   ← status and decisions
  app-design.md / tfy-design.md           ← current design
  sketches/                               ← deferred pilot designs (WIP)
  tools/                                  ← migration scripts, simulator (WIP)
```

APP format standard: [`../../standard/app-authoring.md`](../../standard/app-authoring.md). Reference instances: [`../../examples/`](../../examples/).

For current phase, priorities, pilot status, and decisions, read `teamfoundry-stack-realignment-plan.md`.

## Read Order

1. `teamfoundry-stack-realignment-vision.md` — baseline strategic thesis; stable after acceptance
2. `teamfoundry-stack-realignment-plan.md` — status, work patterns, pillars, design decision logs
3. `app-design.md` — current APP design
4. `tfy-design.md` — current TeamFoundry design, translation flow, simulator model

When the vision and plan disagree on implementation details, follow the plan design decision logs and the current design documents.

## Document Roles

| Document | Role | Update frequency |
| --- | --- | --- |
| Vision | Why the realignment exists; initial stack model and roadmap pillars | Rarely; baseline only |
| Plan | Status, coordination, work patterns, design decision logs | Frequently |
| APP design | Current APP-owned behavior contract model | As design changes |
| TFY design | Current TeamFoundry-owned consumption, assembly, translation, simulator model | As design changes |
| This README | How to use this folder | Infrequently |

Design documents are current-state only. They do not narrate history. Meaningful design pivots belong in the APP and TFY design decision log tables in the plan.

## Adjacent Repositories

Side-by-side clones on the same workstation:

```text
C:\code\agent-playbook-pack
C:\code\teamfoundry.ai
C:\code\openclaw
```

This is a temporary working-context assumption, not a monorepo, submodule layout, or permanent dependency relationship.

## TeamFoundry Reference Map

Use these entry points when reading `teamfoundry.ai`:

| Path | Use for |
| --- | --- |
| `docs/TeamFoundry-Product-Documentation.md` | Foundry, Forge, HQ model |
| `foundry/ops/inventories/skills/` | Agent Skills-shaped TFY skills |
| `foundry/ops/casts/` | Base casts such as `teamfoundry-employee` |
| `forge/ops/agents-forged/Warren/` | Forged assistant example |
| `forge/ops/agents-forged/Warren/inventories/habits/` | Scheduled behavior examples |
| `foundry/ops/inventories/skills/hq-requests/` | HQ request intake behavior |

## APP Framework References

| Path | Use for |
| --- | --- |
| `standard/app-authoring.md` | Authoritative APP standard |
| `documentation/framework.md` | APP concepts (editorial) |
| `documentation/naming.md` | Naming rationale and history |
| `examples/` | Reference `{packId}.app/` instances |

Program-only material (not APP format standard):

| Path | Use for |
| --- | --- |
| `sketches/teamfoundry-employee-base/` | Deferred TFY pilot design sketch |
| `tools/tfy-simulator/` | Local TFY simulator harness |
| `tools/migrate-trading-coach.py` | Regenerate `examples/trading-coach.app/` from legacy source |

Paths above are relative to this folder (`documentation/tfy-stack-realignment/`).

## How To Use This Folder

- Read the plan before starting work.
- Use design documents for current APP or TFY design boundaries.
- Use example directories for pack design reference; verify file existence on disk or in the plan before assuming materialization.
- Record status, decisions, and next actions only in the plan document.
