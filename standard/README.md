# Standard

Normative APP standard files.

| File | Purpose |
| --- | --- |
| [`app-authoring.md`](app-authoring.md) | Authoring standard — layout, layers, execution outcomes |
| [`pack.manifest.schema.json`](pack.manifest.schema.json) | JSON Schema for `pack.app.yaml` |
| [`playbook.manifest.schema.json`](playbook.manifest.schema.json) | JSON Schema for `playbook.app.yaml` |
| [`validate-manifests.py`](validate-manifests.py) | Validate example manifests (YAML parse → schema check) |
| [`requirements.txt`](requirements.txt) | Python dependencies for `validate-manifests.py` |

Manifests are **YAML on disk**; schemas are **JSON** for validation tooling.

Reference instances: [`../examples/`](../examples/). Product guide: [`../documentation/app-workbench-guide.md`](../documentation/app-workbench-guide.md).
