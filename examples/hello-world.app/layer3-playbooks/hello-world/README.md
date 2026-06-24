# Hello World Playbook

## Playbook Id

`hello-world`

## Playbook Report Id

`HelloWorld`

## Composition

```text
requires:
  - layer0-workflows/input-discovery
uses:
  - layer1-skills/compose-greeting
overlays:
  - layer2-overlays/welcome-banner.md          when banner: true
  - overlays/friendly-sign-off.md              when friendly: true
gates:
  - inputs-resolved
  - output-written
```

## Inputs

| Input | Type | Default | Description |
| --- | --- | --- | --- |
| `recipient` | string | `World` | Name to greet |
| `friendly` | boolean | `false` | Apply playbook-scoped sign-off overlay |
| `banner` | boolean | `false` | Apply pack-level welcome banner overlay |

## Core Output Phase

Run `input-discovery`, clear `inputs-resolved`, execute `compose-greeting`, write the **Greeting** section to `Report.md`.

## Augmented Output Phase

When `banner: true`, apply pack-level `welcome-banner` overlay before the greeting section.

When `friendly: true`, apply playbook-scoped `friendly-sign-off` overlay after the greeting section.

## Output Artifacts

```text
{userDatastore}/runs/<GenerationTimestamp>-HelloWorld/
  Report.md
  run-manifest.yaml
```

See `contracts/output-artifact-contract.md`.
