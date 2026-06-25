# AgentPlaybookPack — APP Standards Workbench

Entry point for the workbench. Defines the APP format. **Not** an APP distribution repo.

**APP** (AgentPlaybookPack) packages domain playbooks that compose [Agent Skills](https://agentskills.io), workflows, contracts, gates, overlays, and manifests into runnable user-intent jobs.

---

## Workbench layout

```text
agent-playbook-pack/
  README.md           ← this file (workbench map)
  standard/           ← normative APP standard
  examples/           ← reference pack instances
  documentation/      ← developer docs and TFY program (not APP standard)
```

```text
Distribution repo (published product)     Pack instance ({packId}.app/)
my-product-app/                           pack.app.yaml
  README.md                               README.md
  hello-world.app/                        layer0-workflows/
  trading-coach.app/                      layer1-skills/
                                          layer2-overlays/
                                          layer3-playbooks/
                                          contracts/
```

| Term | Meaning |
| --- | --- |
| **Standards Workbench** | This repo |
| **Distribution repo** | `README.md` + `*.app/` only; clients pull read-only copies |
| **Pack instance** | `{packId}.app/` — the behavior unit |
| **`userDatastore`** | User persistent data — bound at execution; never in APP repos |

---

## File scope

| Path | Scope |
| --- | --- |
| [`README.md`](README.md) | Workbench identity, layout, vocabulary (this file) |
| [`standard/app-authoring.md`](standard/app-authoring.md) | Authoritative APP standard |
| [`standard/README.md`](standard/README.md) | Standard folder label |
| [`examples/`](examples/) | Reference pack instances |
| [`documentation/`](documentation/) | Workbench developer docs; not APP execution standard |
| [`documentation/tfy-stack-realignment/`](documentation/tfy-stack-realignment/) | TeamFoundry program — not APP format |

---

## TeamFoundry realignment

Temporary program in [`documentation/tfy-stack-realignment/`](documentation/tfy-stack-realignment/). Status: [`teamfoundry-stack-realignment-plan.md`](documentation/tfy-stack-realignment/teamfoundry-stack-realignment-plan.md).
