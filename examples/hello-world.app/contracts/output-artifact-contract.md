# Hello World Output Artifacts

## Run folder pattern

```text
{userDatastore}/runs/<GenerationTimestamp>-HelloWorld/
```

| Token | Format |
| --- | --- |
| `GenerationTimestamp` | `YYYYMMDD-HHMMSS` (wall-clock at folder creation) |
| `HelloWorld` | Fixed playbook report id |

Example:

```text
{userDatastore}/runs/20260623-143052-HelloWorld/
```

## Required artifacts

| File | Role |
| --- | --- |
| `Report.md` | Self-contained human-readable run output |
| `run-manifest.yaml` | Structured canonical run record |

## Report.md

Minimum sections:

1. **Greeting** — core output from `compose-greeting` skill
2. **Welcome banner** — present only when `banner: true` (pack-level overlay)
3. **Sign-off** — present only when `friendly: true` (playbook-scoped overlay)
4. **Appendix: Inputs Resolved** — final resolved playbook inputs

## run-manifest.yaml

Record pack id, playbook id, versions, timestamps, resolved inputs, skills executed, overlays executed, and output paths. Align field names with `schema/app-manifest-v0.1.md` run manifest sketch.

## Timestamp rules

- Use actual generation time — no placeholders
- Never overwrite an existing folder; create a new timestamp if the path exists
