# AgentPlaybookPack — APP Standards Workbench

Entry point for humans and agents.

**APP** (AgentPlaybookPack) packages domain playbooks that compose [Agent Skills](https://agentskills.io), workflows, contracts, gates, overlays, and manifests into runnable user-intent jobs.

This repository is the **APP Standards Workbench** — it defines the format. It is **not** an APP distribution repo.

---

## Three repo shapes

```text
Standards Workbench (this repo)          Distribution repo (published product)
agent-playbook-pack/                     my-product-app/
  README.md                                README.md
  docs/          ← format prose             trading-coach.app/
  schema/        ← manifest draft           other-pack.app/
  examples/      ← reference instances
  docs/tfy-stack-realignment/  ← TFY program only (not APP format)
```

A **pack instance** is a `{packId}.app/` folder. Same shape in `examples/` (reference) and in a distribution repo (published):

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

| Term | Meaning |
| --- | --- |
| **Standards Workbench** | This repo — format definition and reference instances |
| **Distribution repo** | Separate repo per product — `README.md` + `{packId}.app/` only; clients pull read-only copies |
| **Pack instance** | `{packId}.app/` — the behavior unit |
| **`userDatastore`** | User persistent data — bound at execution; never in APP repos |

---

## The standard

The format reference is **[`examples/hello-world.app/`](examples/hello-world.app/)** — a minimal instance with every APP shape.

To **run** a pack (here or in a distribution repo): read **`{packId}.app/APP-EXECUTION.md`**, then follow manifests.

---

## File scope (this repo)

Each path has one job. Do not duplicate content across files.

| Path | Scope |
| --- | --- |
| [`README.md`](README.md) | Repo identity, shapes, vocabulary (this file) |
| [`docs/framework.md`](docs/framework.md) | APP concepts and layer model |
| [`docs/app-execution.md`](docs/app-execution.md) | Execution contract — canonical source for instance `APP-EXECUTION.md` |
| [`docs/app-skills.md`](docs/app-skills.md) | `layer1-skills/` standard and playbook skill composition |
| [`docs/pack-store.md`](docs/pack-store.md) | Future Pack Store draft (not current standard) |
| [`schema/app-manifest-v0.1.md`](schema/app-manifest-v0.1.md) | Manifest field draft |
| [`examples/hello-world.app/`](examples/hello-world.app/) | Format reference — all shapes |
| [`examples/trading-coach.app/`](examples/trading-coach.app/) | Domain reference; TFY dev convenience; graduates to distribution repo |
| [`docs/tfy-stack-realignment/`](docs/tfy-stack-realignment/) | TeamFoundry realignment program — not APP format |

---

## TeamFoundry realignment

Temporary program in [`docs/tfy-stack-realignment/`](docs/tfy-stack-realignment/). Not part of the APP format. Status: [`teamfoundry-stack-realignment-plan.md`](docs/tfy-stack-realignment/teamfoundry-stack-realignment-plan.md).
