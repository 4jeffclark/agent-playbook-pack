# Agent playbook execution for Alice
_Exported on 6/28/2026 at 08:30:37 MST from Cursor (3.9.8)_

---

**User**


please learn: https://github.com/4jeffclark/agent-playbook-pack

Run hello world (https://github.com/4jeffclark/hello-world-app) for Alice with user storage at UserData/alice. Use your existing cursor workspace for agent workspace.

---

**Cursor**

I'll pull the agent-playbook-pack and hello-world-app repos and inspect this workspace so we can run hello-world for Alice under `UserData/alice`.


Fetching the repos for playbook instructions and scanning the workspace.


Executing the hello-world playbook for Alice: binding storage to `UserData/alice` and running the compose-greeting skill.


Hello World for **Alice** is done using the [hello-world-app](https://github.com/4jeffclark/hello-world-app) distribution and the [APP Standards Workbench](https://github.com/4jeffclark/agent-playbook-pack) execution model.

### Bindings

| Input | Path |
| --- | --- |
| `userDatastore` | `UserData/alice` |
| `agentWorkspace` | `c:\code\app-test-agent` (this workspace) |

### Resolved inputs

| Input | Value | Status |
| --- | --- | --- |
| `recipient` | Alice | confirmed |
| `friendly` | false | default |
| `banner` | false | default |

### Execution

1. **input-discovery** — parsed “Alice” from your request; overlays left at defaults.
2. **compose-greeting** — ran `scripts/run.py` with `--recipient Alice`.
3. **Overlays** — skipped (`friendly` and `banner` are false).
4. **Primary output** — report written per the output contract.

### Output

Report:

`UserData/alice/reports/20260627-133810-HelloWorld/Report.md`

```markdown
## Greeting

Hello, Alice!
```

Intermediate skill artifacts in the agent workspace: `greeting.txt` and `skill-result.json`.

To rerun with overlays, for example: *Run hello world for Alice with a friendly sign-off and welcome banner.*

---

**User**

Run hello world again for Bob with a friendly sign-off and welcome banner, with user storage at UserData/bob. 

---

**Cursor**

Running hello-world for Bob with both overlays and storage under `UserData/bob`.


Hello World for **Bob** is complete with both overlays enabled.

### Bindings

| Input | Path |
| --- | --- |
| `userDatastore` | `UserData/bob` |
| `agentWorkspace` | `c:\code\app-test-agent` |

### Resolved inputs

| Input | Value | Status |
| --- | --- | --- |
| `recipient` | Bob | confirmed |
| `friendly` | true | confirmed |
| `banner` | true | confirmed |

### Output

Report written to:

`UserData/bob/reports/20260627-134441-HelloWorld/Report.md`

It includes the **Welcome banner** and **Sign-off** overlays, the core greeting (`Hello, Bob!`), and the **Appendix: Inputs Resolved** section.

---

**User**

Run hello world  for Carol with a welcome banner only, with user storage at UserData/carol. Use your existing cursor workspace for agent workspace.

---

**Cursor**

Hello World for **Carol** is done with the welcome banner only (no friendly sign-off).

### Bindings

| Input | Path |
| --- | --- |
| `userDatastore` | `UserData/carol` |
| `agentWorkspace` | `c:\code\app-test-agent` |

### Resolved inputs

| Input | Value | Status |
| --- | --- | --- |
| `recipient` | Carol | confirmed |
| `friendly` | false | default |
| `banner` | true | confirmed |

### Output

Report written to:

`UserData/carol/reports/20260627-134847-HelloWorld/Report.md`

It includes the **Welcome banner**, core greeting (`Hello, Carol!`), and **Appendix: Inputs Resolved**. The **Sign-off** section was omitted because `friendly` stayed at its default.

---

**User**

Run hello world for Dan with a friendly sign-off only, with user storage at UserData/dan. Use your existing cursor workspace for agent workspace.

---

**Cursor**

Hello World for **Dan** is complete with the friendly sign-off only (no welcome banner).

### Bindings

| Input | Path |
| --- | --- |
| `userDatastore` | `UserData/dan` |
| `agentWorkspace` | `c:\code\app-test-agent` |

### Resolved inputs

| Input | Value | Status |
| --- | --- | --- |
| `recipient` | Dan | confirmed |
| `friendly` | true | confirmed |
| `banner` | false | default |

### Output

Report written to:

`UserData/dan/reports/20260627-135045-HelloWorld/Report.md`

It includes the core greeting (`Hello, Dan!`), the **Sign-off** overlay, and **Appendix: Inputs Resolved**. The **Welcome banner** section was omitted because `banner` stayed at its default.

---

**User**

please execute the source profile playbook included in this pack: https://github.com/4jeffclark/portfolio-coach-app.git User data is in:   @PortfolioCoach 

---

**Cursor**

Cloning the portfolio-coach-app pack and locating the PortfolioCoach user data to run the source profile playbook.


Setting up the expected `data/` layout (junctions to existing `raw/` and `canonical/`), then running the playbook skills.


Source profile playbook from [portfolio-coach-app](https://github.com/4jeffclark/portfolio-coach-app) is complete.

### Bindings

| Input | Path |
| --- | --- |
| `userDatastore` | `UserData/jclark/PortfolioCoach` |
| `agentWorkspace` | `c:\code\app-test-agent` |

### Resolved inputs

| Input | Value | Status |
| --- | --- | --- |
| `evaluation` | true | default |
| `analysisPeriodStart` | 20210827 | default (full available range) |
| `analysisPeriodEnd` | 20260616 | default (full available range) |

No analysis period was specified, so the full canonical date range was used (2021-08-27 through 2026-06-16).

### Workflows

1. **datastore-merge-and-validate** — No new session attachments in `inputs/`. Validated 12 raw files against `ingestion_manifest.csv`; canonical tables already rebuilt (2026-06-16).
2. **structured-input-discovery** — Inputs resolved with evaluation enabled and full-range defaults.

### Skills executed

- `datastore-inventory` — inventory, account coverage, metrics
- `source-profile-insights` — scorecard (evaluation overlay)
- `exit-interview` — review prompts (evaluation overlay)

### Output

Report folder:

`UserData/jclark/PortfolioCoach/reports/20260628-080448-SourceProfile-20210827-20260616/`

| Artifact | Description |
| --- | --- |
| `Report.md` | Full inventory profile (5 sections) + evaluation |
| `DataStoreInventory.csv` | Raw and canonical inventory |
| `AccountCoverage.csv` | Per-account order coverage |
| `Metrics.csv` | Summary counts |
| `SourceProfileScorecard.md` | Coverage/quality scorecard |
| `ExitInterview.md` | Review prompts (user responses pending) |

### Highlights

- **3 accounts** covered (Traditional IRA x7232, Brokerage x7782, Partnership x0142)
- **12 raw exports** across all four E*TRADE types
- **2,904** deduplicated orders (2024-06-24 → 2026-06-16)
- **2,356** merged account-history rows (2021-08-27 → 2026-06-16)
- **109** open-position symbols in latest snapshot

**Note:** Junctions were added at `data/raw` and `data/canonical` so the pack’s `pc-lib` can resolve paths per the [datastore contract](https://github.com/4jeffclark/portfolio-coach-app). Your existing `raw/` and `canonical/` folders were not moved.

To rerun for a specific period (e.g. May 2026) or without evaluation: *Run a source profile for May 2026* or *Profile my datastore without the evaluation overlay.*

---

**User**

I am a developer testing the APP concept and POC implementation. You are my first test execution agent. Based on your experience with the standard and these first two packs, please provide your feedback on your experience using the workbench and packs

---

**Cursor**

Here is candid feedback from acting as your first execution agent across the [APP Standards Workbench](https://github.com/4jeffclark/agent-playbook-pack), [hello-world-app](https://github.com/4jeffclark/hello-world-app), and [portfolio-coach-app](https://github.com/4jeffclark/portfolio-coach-app).

---

## Overall impression

The concept works. APP gave me enough structure to execute repeatable, auditable runs without a custom orchestrator. The layer model (workflows → skills → overlays → outputs) maps cleanly to how an agent actually thinks: resolve inputs, run prerequisites, execute core logic, optionally augment, write artifacts to the user datastore.

Hello World proved the format end-to-end in minutes. PortfolioCoach showed where the standard scales—and where execution still depends heavily on agent judgment and conventions that are not fully machine-checkable.

---

## What worked well

### 1. Clear separation of concerns

The distinction between:

- **Behavior repo** (pack manifests, skills, contracts)
- **`userDatastore`** (persistent user data and reports)
- **`agentWorkspace`** (intermediate artifacts)

…is the strongest design choice. It kept hello-world runs for Alice/Bob/Carol/Dan cleanly isolated under `UserData/<user>/` while reusing the same workspace. That matches how real products will run.

### 2. Natural-language input discovery

Parsing “Bob with a friendly sign-off and welcome banner” into `recipient`, `friendly`, and `banner` felt natural. The structured-input-discovery workflow matches how users will actually talk. Defaults (`friendly: false`, `banner: false`) were easy to apply when unstated.

### 3. Playbook manifests as execution contracts

Reading `pack.app.yaml` → `<playbook-id>.app.yaml` → referenced artifacts was a reliable read order. I always knew:

- What inputs to bind
- What workflows to run first
- What skill scripts to invoke
- Which overlays apply and when
- Where outputs go

The `pathTemplate` with `{userDatastore}`, `{timestamp}`, and input tokens is concrete enough to implement without guessing.

### 4. Hello World as a calibration pack

Hello World is an excellent reference instance. It exercises every layer without hiding complexity:

- One workflow, one skill, two overlays, one report contract
- A real script with workspace outputs
- Overlay gating via boolean inputs

If a new execution agent can run Hello World correctly, they understand APP.

### 5. Skills + scripts pattern

The `SKILL.md` → `scripts/run.py` pattern is pragmatic. Prompt-first with optional scripts is the right default. Hello World’s `compose-greeting` script did exactly what the skill promised and left report composition to the agent, which matches the fire-and-forget model.

### 6. Contracts as durable rules

`output-artifact-contract.md` and `user-datastore-layout.md` answered “what must exist in the report folder?” without duplicating that logic in YAML. That separation keeps manifests thin and contracts readable.

---

## Friction and gaps

### 1. Pack bootstrap is undefined for execution agents

There is no standard way for an execution agent to *obtain* a pack at runtime. I cloned repos into `.hello-world-app-tmp` and `.portfolio-coach-app-tmp` ad hoc. For a POC that is fine; for a product you will want one of:

- Pack pinned in workspace (submodule, vendor folder)
- Pack URL + version in a run request
- A small “execution bootstrap” doc: *clone this repo, bind these paths, run this playbook*

The workbench defines authoring well; distribution consumption is still agent-improvised.

### 2. User datastore layout drift vs. tooling assumptions

PortfolioCoach data lived at:

```text
PortfolioCoach/raw/etrade/
PortfolioCoach/canonical/
```

But the contract and `pc-lib` expect:

```text
PortfolioCoach/data/raw/etrade/
PortfolioCoach/data/canonical/
```

`ingestion_manifest.csv` paths referenced `data\raw\etrade\...` while files sat one level up. I fixed this with Windows junctions under `data/`. That worked, but an execution agent should not need filesystem surgery.

**Recommendation:** Either enforce layout at validation time, or make `pc-lib` resolve both legacy and standard layouts explicitly and document the precedence rule.

### 3. Workflows and gates are behavioral, not verifiable

Gates like `inputs-resolved`, `datastore-merge-complete`, and `output-written` are declared in YAML but nothing checks that I cleared them. I self-attested compliance. For Hello World that is harmless; for PortfolioCoach merge/validate it matters more.

**Recommendation:** Add lightweight gate checkpoints in skill scripts or a post-run validator:

- “Does report folder exist?”
- “Do required CSVs exist?”
- “Does `ingestion_manifest` hash match raw files?”

Even a optional `validate-run.py` would strengthen the POC.

### 4. PortfolioCoach skills are scaffolds; the agent still writes the report

`datastore-inventory` produced useful CSVs. `source-profile-insights` and `exit-interview` produced thin templates. I wrote most of `Report.md` by re-reading the skill procedure (5 inventory sections) and querying canonical data myself.

That is acceptable for a POC, but the boundary between “skill output” and “agent synthesis” was unclear:

| Skill | Script output | Agent work remaining |
| --- | --- | --- |
| `compose-greeting` | Complete greeting text | Report assembly only |
| `datastore-inventory` | CSV indexes | Full narrative sections 1–5 |
| `source-profile-insights` | 3-line scorecard stub | Entire evaluation narrative |
| `exit-interview` | Question template | All answers |

**Recommendation:** For domain packs, either:

- Push more quantified sections into skill scripts (markdown fragments ready to embed), or
- Explicitly label skills as `scaffold` vs `complete` in `SKILL.md` so agents know how much synthesis is expected

### 5. Analysis period defaults are ambiguous

For source-profile, no period was specified. The workflow says ask the user; fire-and-forget execution says proceed. I defaulted to full available range (2021-08-27 → 2026-06-16). That was reasonable but not uniquely determined—May 2026 would also have been valid.

**Recommendation:** Add a playbook-level default policy in the manifest or workflow, e.g.:

- `defaultPeriod: fullAvailableRange`
- `defaultPeriod: latestCalendarMonth`

So agents do not invent policy.

### 6. Skill script quality bug (minor but trust-eroding)

`DataStoreInventory.csv` showed orders date range as 2026-06-14 → 2026-06-16 because the inventory skill scanned the wrong date column (`ExportedAtLocal` before `Date`). Ingestion manifest correctly showed 2024-06-24 → 2026-06-16. I had to cross-check manually.

Small inconsistencies undermine confidence in “run the script and trust the CSV.”

### 7. Agent workspace hygiene

Repeated runs left artifacts in the workspace root:

- `greeting.txt`, `skill-result.json`
- `datastore-inventory/`, `source-profile-insights/`, `exit-interview/`

There is no contract for workspace cleanup or run-scoped subfolders (e.g. `{agentWorkspace}/runs/{timestamp}/`). Over time, concurrent or repeated runs could collide or confuse.

**Recommendation:** Document a workspace layout convention, or pass `--workspace` to a per-run subdirectory.

### 8. Windows execution environment

Minor but real: PowerShell does not accept `&&`, Python paths need care, junctions differ from symlinks. The standard says “runtime-neutral” but examples assume Unix shell quoting (`$USER_DATASTORE`). A one-line Windows equivalent in skill docs would help.

---

## Workbench vs. packs: division of labor

| Concern | Workbench | Execution experience |
| --- | --- | --- |
| Authoring standard | Strong — `app-authoring.md` was sufficient | Read once, then referenced manifests |
| Reference instance | Hello World in `examples/` matched distribution repo | Good parity |
| Validation tooling | `validate-manifests.py` exists | I did not run it during execution; unclear if execution agents should |
| Human guide | `app-workbench-guide.md` | Useful context, not needed at runtime |
| Agent instructions in README | Clear read order for workbench vs execution agents | Helped orient quickly |

The workbench successfully taught me the format. What is still thin is the **execution agent playbook**—a short doc like:

1. Bind `userDatastore` and `agentWorkspace`
2. Load pack from distribution repo
3. Read manifests in order
4. Run workflows → skills → overlays
5. Write outputs per contract
6. (Optional) validate output folder

That would complement the authoring standard.

---

## Comparative notes: Hello World vs PortfolioCoach

**Hello World** felt “complete.” I could trace every step from user utterance to report file with minimal improvisation. It is a good proof that APP is executable without an engine.

**PortfolioCoach** felt “half scripted, half spec.” The contracts are rich (especially `datastore-contract.md`), but executable coverage lags the prose. Merge/rebuild is described in detail in the contract but not implemented in shipped scripts—the agent is expected to satisfy it by inspection and judgment. For a POC that is honest; for production you will want either:

- A `datastore-merge` skill script, or
- Explicit scope: *“execution agent validates existing canonical; does not rebuild”*

---

## Suggestions prioritized for the POC

**High impact, low effort**

1. Add an **Execution Agent Guide** (1–2 pages) to the workbench—not more standard prose, but operational steps.
2. Add **output folder validation** (required files exist, paths match template).
3. Fix **datastore path resolution** in `pc-lib` for layout mismatches.
4. Document **default analysis period** behavior in source-profile workflow.

**Medium effort**

5. Expand `datastore-inventory` to emit **Report.md section fragments** (or a `report-sections.json`) so the agent embeds rather than rewrites.
6. Standardize **per-run workspace directories**.
7. Mark skills with **`outputCompleteness: scaffold | complete`** in frontmatter.

**Longer term**

8. Pack registry / pin mechanism (URL + commit + playbook id in run request).
9. Optional gate enforcement in a thin runner CLI that wraps skill scripts.

---

## What I would tell another execution agent

> Read `standard/app-authoring.md` once. Clone the distribution repo. Bind user data and workspace. Start from `pack.app.yaml` and the playbook manifest—do not read the whole pack tree. Run scripts when `SKILL.md` says so; compose the report from skill outputs and contracts. Treat workflows and gates as a checklist you self-verify. When contracts and on-disk layout disagree, trust raw files and call out the mismatch in the report.

That workflow is viable today. Hello World validates the concept; PortfolioCoach validates that domain complexity needs stronger scripting and validation to match the quality of the written contracts.

---

## Bottom line

APP is a credible POC format. The workbench gives authors a clear grammar; distribution repos give execution agents a readable program. The main gap is not the YAML/manifest design—it is **operational closure**: bootstrap, layout enforcement, script completeness, and post-run validation.

Hello World demonstrates the idea works. PortfolioCoach demonstrates where the agent still carries too much implicit domain work. Closing that gap is the natural next iteration before calling this production-ready.

If useful, I can turn this into a structured issue list for the workbench repo or draft an **Execution Agent Guide** section you could add to `documentation/`.

---

**User**

Please restate your feedback in full detail but organize your output to separately deliver your feedback on the APP standard itself, the authoring of hello-world, and the authoring of portfolio-coach.

---

**Cursor**

## Feedback on the APP standard itself

This section covers the workbench ([agent-playbook-pack](https://github.com/4jeffclark/agent-playbook-pack)), normative standard (`standard/app-authoring.md`), manifest schemas, layer model, contracts, and what it is like to execute *any* pack as an agent.

### What the standard gets right

**Separation of behavior, user data, and workspace**

The three-way split is the strongest design decision in APP:

| Role | Bound at execution | In pack repo? |
| --- | --- | --- |
| Behavior contract | Read from distribution repo | Yes |
| `{userDatastore}` | User persistent storage | No |
| `{agentWorkspace}` | Agent temp / intermediate artifacts | No |

That model worked cleanly across all runs. Hello World for Alice, Bob, Carol, and Dan each wrote reports under their own `UserData/<user>/` while reusing the same Cursor workspace. PortfolioCoach wrote under `UserData/jclark/PortfolioCoach/reports/` without polluting the pack repo. This is the right foundation for a real product.

**Layer model maps to agent cognition**

The 0→3 layering (workflows → skills → overlays → playbooks) matches how an agent naturally executes:

1. Resolve and confirm inputs (layer 0)
2. Run prerequisite infrastructure (layer 0)
3. Execute core capabilities (layer 1)
4. Apply optional augmentations (layer 2)
5. Write durable outputs (layer 3 manifest + contracts)

I never felt confused about *where* to look for authority. Manifests say what to compose; contracts say what outputs must look like; skills say how to run scripts.

**Fire-and-forget is the right scope boundary**

APP supplies behavioral instructions and stops. It does not try to be an orchestrator, run tracker, or state machine. That keeps the format portable across Cursor, CLI, CI, or future engines. I could execute entirely from manifests + skills + contracts without needing APP to "stay involved" after the report was written.

**Manifest read order is deterministic**

The prescribed sequence worked every time:

1. `pack.app.yaml` — bind pack-level inputs, discover playbooks
2. `layer3-playbooks/<id>/<id>.app.yaml` — resolve playbook inputs, composition, gates, outputs
3. Manifest-referenced artifacts only — workflows, skills, overlays, contracts

I did not need to crawl the whole pack tree. That is essential for agents with limited context windows.

**Composition verbs are expressive enough**

`requires`, `uses`, `overlays`, and gate metadata on the playbook manifest covered every composition need I encountered. Overlay `when:` conditions (`banner == true`, `evaluation == true`) were easy to evaluate from natural language.

**Contracts as cross-cutting rules**

Keeping durable layout, artifact shape, and naming rules in `contracts/` rather than duplicating them in YAML was correct. When assembling report folders, I consulted contracts for:

- Required files
- Folder naming tokens
- Timestamp rules
- Section minimums

Manifests stayed thin; contracts stayed readable.

**Natural-language input discovery**

The layer 0 input-discovery pattern (parse → summarize → reconcile → confirm) matched real user utterances well:

- "Run hello world for Alice"
- "Bob with a friendly sign-off and welcome banner"
- "Carol with a welcome banner only"
- "Dan with a friendly sign-off only"

Users do not need parameter syntax. Defaults (`friendly: false`, `banner: false`, `evaluation: true`) were easy to apply when unstated.

**agentskills.io alignment for layer 1**

Using standard Agent Skills (`SKILL.md`, optional `scripts/`, `references/`) rather than inventing a parallel skill format was wise. APP composes skills; it does not redefine them. The `Procedure` / `Scripts` / `Outputs` sections in skill docs were sufficient to decide when to run bundled Python vs. synthesize in the agent.

**Workbench vs. distribution repo distinction**

The workbench README clearly separates:

- **Workbench agent** — learn standard, validate, author packs
- **Execution agent** — consume distribution repos only

That role split prevented me from treating `examples/` as an execution target. Cloning `hello-world-app` and `portfolio-coach-app` as distribution repos felt architecturally correct.

---

### Gaps and friction in the standard

**1. No execution-agent operational guide**

The authoring standard (`app-authoring.md`) is strong. What is missing is a short, normative **execution guide** — not more format rules, but operational steps:

1. Obtain pack (distribution repo + version)
2. Bind `{userDatastore}` and `{agentWorkspace}`
3. Read manifests in order
4. Execute workflows → skills → overlays
5. Write outputs per contract
6. Self-verify gates / optional validation

The workbench README has agent instructions for *authoring*; execution agents still improvise bootstrap and verification.

**2. Pack bootstrap is undefined**

There is no standard way to obtain a pack at runtime. I cloned repos into ad hoc folders (`.hello-world-app-tmp`, `.portfolio-coach-app-tmp`). For a POC that works; for a product you need one of:

- Pack pinned in workspace (submodule, vendor path)
- Pack URL + commit/ref in the run request
- A registry or install command

The standard defines *shape* well; *provisioning* is out of scope today.

**3. Gates are declared but not enforceable**

Gates like `inputs-resolved`, `datastore-merge-complete`, and `output-written` live on the playbook manifest, but nothing verifies they were cleared. I self-attested compliance. For Hello World that is harmless; for PortfolioCoach merge/validate it matters more.

**Recommendation:** Optional post-run validation — required files exist, paths match template, manifest hashes match raw files. Could be a thin `validate-run.py` referenced from the standard without turning APP into an orchestrator.

**4. Workflow procedures are honor-system**

Layer 0 workflows describe *what* to do in prose. An agent reads them and claims to have followed them. There is no machine-checkable handshake between workflow completion and gate clearing.

This is consistent with fire-and-forget, but the standard could clarify:

- Which workflows *must* have companion scripts vs. agent-only procedures
- What minimum evidence constitutes "gate cleared" (e.g., a range summary artifact)

**5. Default input policies are underspecified**

When the user does not specify an analysis period, structured-input-discovery says reconcile with the user — but fire-and-forget execution proceeds. I defaulted PortfolioCoach to full available range (2021-08-27 → 2026-06-16). That was reasonable but not uniquely determined; May 2026 would also have been valid.

The standard should allow playbooks to declare default resolution policy:

- `defaultPeriod: fullAvailableRange`
- `defaultPeriod: latestCalendarMonth`
- `defaultPeriod: requireExplicit`

Without this, agents invent policy.

**6. `{agentWorkspace}` layout is unconstrained**

Repeated runs left artifacts in the workspace root and skill-named subdirectories (`greeting.txt`, `skill-result.json`, `datastore-inventory/`, etc.). There is no convention for:

- Per-run subfolders (`runs/{timestamp}/`)
- Cleanup between runs
- Collision avoidance for concurrent runs

The standard binds `{agentWorkspace}` but does not define its internal shape.

**7. Runtime neutrality vs. shell examples**

The standard claims runtime-neutral execution, but skill docs use Unix-style examples (`$USER_DATASTORE`, `$AGENT_WORKSPACE`). On Windows PowerShell, `&&` fails, path quoting differs, and junctions may substitute for symlinks. Minor, but real for a POC tested on Windows.

**Recommendation:** One cross-platform invocation block per skill, or document that scripts accept `--datastore` / `--workspace` as the canonical interface (which they do — the shell variable examples are just ergonomics).

**8. Validation tooling role is ambiguous**

`validate-manifests.py` exists for authoring. It is unclear whether execution agents should run it before executing a distribution repo, or whether that is author/CI-only. A one-line note in the standard would help.

**9. Discovery mode vs. execution mode**

The standard defines discovery, execution, and factory modes. Boundaries are clear in prose ("discovery must not read datastore or write reports"). In practice, an agent learning a new pack may blur discovery and execution in one session — as I did when cloning the workbench to learn, then immediately executing distribution repos. A sharper handoff cue in the standard would help ("after discovery, confirm intent before binding userDatastore").

**10. Skill output completeness is unspecified**

The standard says skills produce outputs listed in `SKILL.md`, but does not distinguish:

- **Complete outputs** — script produces final artifact content
- **Scaffold outputs** — script produces structure; agent fills narrative

That ambiguity becomes painful in domain packs (PortfolioCoach). The standard could add optional frontmatter: `outputCompleteness: complete | scaffold`.

---

### Standard-level recommendations (prioritized)

| Priority | Recommendation |
| --- | --- |
| High | Add an **Execution Agent Guide** to `documentation/` (operational, not authoring) |
| High | Define **default input resolution policies** for playbooks with date/period inputs |
| High | Optional **post-run output validation** against contract + path template |
| Medium | Document **`{agentWorkspace}` layout** convention (per-run subdirs) |
| Medium | Clarify **gate evidence** — what artifact or check clears each gate |
| Medium | Add **`outputCompleteness`** hint on skills |
| Lower | Cross-platform script invocation examples |
| Lower | Pack provisioning convention (URL + ref + playbook id) |

---

### Bottom line on the standard

APP is a credible, portable format. The layer model, manifest read order, three-way data separation, and contract-driven outputs form a coherent grammar that an agent can execute without a custom engine. Hello World proves the grammar works.

The main gap is **operational closure**: bootstrap, layout enforcement at the `{userDatastore}` boundary, gate verification, default policies, and workspace conventions. The standard teaches authors how to write packs well; it does not yet teach execution agents how to *close* a run with the same rigor.

---

## Feedback on hello-world authoring

This covers the [hello-world-app](https://github.com/4jeffclark/hello-world-app) distribution repo and its relationship to the workbench reference instance in `examples/hello-world.app/`.

### What hello-world does well

**1. It is a complete end-to-end calibration pack**

Hello World exercises every APP shape in minimal form:

| Layer | Artifact | Purpose |
| --- | --- | --- |
| 0 | `input-discovery.md` | Parse natural language inputs |
| 1 | `compose-greeting` skill + `run.py` | Core output via script |
| 2 | `welcome-banner.md`, `friendly-sign-off.md` | Conditional overlays |
| 3 | `hello-world.app.yaml` | Playbook composition + gates + output path |
| Contracts | output + user-datastore layout | Report shape and user storage rules |

An execution agent can validate understanding of APP by running Hello World once. That is exactly what a reference instance should do.

**2. Skill script does one job completely**

`compose-greeting/scripts/run.py`:

- Takes `--recipient` and `--workspace`
- Writes `greeting.txt` and `skill-result.json`
- Produces the exact greeting text the report needs

The agent's remaining work is assembly (report markdown, copy to userDatastore), not re-derivation of core content. This is the ideal skill/agent division of labor.

**3. Overlay design is intuitive and testable**

Four runs (Alice, Bob, Carol, Dan) naturally exercised the overlay matrix:

| Run | `friendly` | `banner` | Sections in report |
| --- | --- | --- | --- |
| Alice | default false | default false | Greeting only |
| Bob | true | true | Banner + Greeting + Sign-off |
| Carol | default false | true | Banner + Greeting |
| Dan | true | default false | Greeting + Sign-off |

Overlay `when:` conditions mapped directly from user language. No ambiguity.

**4. Input defaults are sensible and documented**

`recipient: World`, `friendly: false`, `banner: false` — all declared in the playbook manifest and repeated in the input-discovery workflow defaults table. When the user said only a name, defaults applied cleanly.

**5. Output contract is tight and achievable**

Required report sections are small and checkable:

1. Greeting (from skill)
2. Welcome banner (overlay only)
3. Sign-off (overlay only)
4. Appendix: Inputs Resolved

Report folder pattern `{userDatastore}/reports/{timestamp}-HelloWorld/Report.md` is simple — no input tokens in the path, which reduces template errors.

**6. User datastore layout is minimal**

```text
{userDatastore}/
  reports/
  inputs/   (optional)
```

No canonical rebuild, no merge workflow, no layout mismatch risk. Perfect for first contact with APP.

**7. Distribution repo parity with workbench example**

The distribution repo structure matched the workbench `examples/hello-world.app/` shape. README "Try it" examples matched how I was invoked. Good author/executor alignment.

**8. Pack README is appropriately lightweight**

User welcome and try-it prompts — not execution authority. I did not need to read it to execute; manifests and contracts were sufficient.

---

### Hello-world friction (minor)

**1. Report assembly is still agent-authored**

The skill produces greeting text; the agent writes `Report.md` structure, Inputs Resolved table, and chooses timestamp for folder creation. That is fine at this scale, but it means "run hello world" is not fully script-closed — an agent must know markdown section order from the output contract.

For Hello World this is acceptable. A `report-assembler` skill or script fragment would be over-engineering.

**2. `skill-result.json` lands in workspace root**

Each run overwrote workspace-level `greeting.txt` and `skill-result.json`. Harmless for sequential single-user tests; would collide under concurrent runs or multi-skill packs.

**3. Input-discovery workflow has no machine output**

The workflow says to present "Inputs Resolved" and clear the `inputs-resolved` gate, but there is no `inputs-resolved.json` artifact. The agent embeds the table in the report from memory. Works, but gate clearing is purely declarative.

**4. No bundled validation of report folder**

After writing `Report.md`, nothing checks required sections exist. At Hello World scale, visual inspection suffices.

---

### Hello-world authoring recommendations

| Item | Suggestion |
| --- | --- |
| Keep as-is | Skill completeness, overlay matrix, contract simplicity |
| Optional | Note in pack README that report assembly is agent responsibility |
| Optional | Example `Inputs Resolved` block in output contract as copy-paste template |
| Do not add | Heavy orchestration, run manifests, or report PDF generation — would fight the minimal purpose |

---

### Bottom line on hello-world

Hello World is an excellent reference pack. It demonstrates that APP is executable without an engine, that natural-language inputs work, that overlays gate correctly, and that user/agent workspace separation scales to multiple users. If every new pack matched Hello World's clarity of skill completeness and contract tightness, APP would feel production-ready for simple playbooks immediately.

---

## Feedback on portfolio-coach authoring

This covers the [portfolio-coach-app](https://github.com/4jeffclark/portfolio-coach-app) distribution repo, the `source-profile` playbook, `pc-lib`, contracts, and execution against `UserData/jclark/PortfolioCoach`.

### What portfolio-coach does well

**1. Domain contracts are exceptionally thorough**

`datastore-contract.md` is the strongest artifact in the pack. It defines:

- Raw vs. canonical semantics
- Export type native shapes and parsing hints
- Account normalization rules (with known account mapping table)
- Canonical schemas for every table
- Incremental merge and dedup keys by export type
- Post-merge validation checklist
- Datastore-aware period selection rules
- Legacy entry limitations

An agent can reason about merge behavior, confidence layers (Observed / Derived / Estimated), and what not to claim about pre-history positions. This is real domain knowledge encoded well.

**2. Playbook manifest composition is clear**

`source-profile.app.yaml` cleanly expresses:

- Two required workflows (merge + input discovery)
- One core skill (`datastore-inventory`)
- One evaluation overlay with `when: evaluation == true`
- Three gates with `after:` phases
- Output path template with analysis period tokens

I knew the execution graph before reading any skill implementation.

**3. Pack-level inputs match the domain**

Requiring `{userDatastore}` with `layoutContract` and `{agentWorkspace}` in `pack.app.yaml` is correct for a datastore-profiling playbook. The binding model scaled from Hello World's simple reports folder to a rich financial datastore.

**4. Layer 0 workflows address real prerequisites**

- `datastore-merge-and-validate` — merge session attachments, rebuild canonical, validate
- `structured-input-discovery` — resolve period and evaluation flag

These reflect actual domain needs that Hello World does not have. The workflow *topics* are right.

**5. Shared `pc-lib` is a good direction**

Centralizing CSV helpers, CLI argument parsing, `skill-result.json` writing, and skill runners in `assets/pc-lib/` avoids duplicating boilerplate across skills. The `--datastore` / `--workspace` CLI interface is consistent.

**6. Evaluation overlay models a second phase well**

When `evaluation: true` (default), the overlay triggers:

- `source-profile-insights` — scorecard
- `exit-interview` — reflection prompts

Separating core inventory from optional evaluation matches the "core output runs without overlays" APP principle.

**7. Report artifact contract specifies a full artifact set**

Primary report folder includes:

- `Report.md`
- `DataStoreInventory.csv`
- `AccountCoverage.csv`
- `Metrics.csv`
- Plus evaluation artifacts when enabled

That gives downstream consumers (human or agent) structured data alongside narrative.

**8. Real user data stress-tested the pack**

Executing against actual E*TRADE exports (12 raw files, 3 accounts, merged canonical tables) surfaced real-world issues — which is what a domain POC should do.

---

### Portfolio-coach friction and gaps

**1. User datastore layout mismatch (critical for execution)**

On disk, data lived at:

```text
PortfolioCoach/raw/etrade/
PortfolioCoach/canonical/
PortfolioCoach/knowledge/
```

The contract and `pc-lib` expect:

```text
PortfolioCoach/data/raw/etrade/
PortfolioCoach/data/canonical/
```

`ingestion_manifest.csv` paths referenced `data\raw\etrade\...` while files sat one level up. `pc-lib/canonical.py` hardcodes:

```python
CANONICAL_DIR = Path("data") / "canonical"
RAW_DIR = Path("data") / "raw" / "etrade"
```

I had to create Windows junctions under `data/` to run skills. An execution agent should not perform filesystem surgery.

**Root cause:** Authoring assumed standard layout; user datastore was populated under a legacy/alternate layout (README in PortfolioCoach also describes `data/` prefix but actual tree did not match).

**Recommendation:**

- `pc-lib` resolves both layouts with documented precedence, or
- A layout validation step fails fast with a clear error, or
- A one-time migration skill normalizes layout

**2. Merge/rebuild workflow is specified in prose but not implemented in scripts**

`datastore-merge-and-validate` and `datastore-contract.md` describe a rigorous merge pipeline (hash check, copy raw, rebuild all canonical, dedup, validate). No shipped skill script performs rebuild. I validated existing canonical state by inspection; I did not rebuild.

For a POC labeled "inventory and quality profile," that may be acceptable if canonical was pre-built. But the playbook *requires* the workflow, creating a gap between spec and executable reality.

**Recommendation:** Either:

- Ship a `datastore-merge` skill with rebuild logic, or
- Narrow workflow scope: *"Validate existing canonical; merge only when session attachments present"*, or
- Mark merge workflow as `agentProcedure: true` with explicit "no rebuild tooling shipped" in pack README

**3. Core skill produces indexes; agent writes the report narrative**

`datastore-inventory/scripts/run.py` via `pc_lib` produced:

- `DataStoreInventory.csv`
- `AccountCoverage.csv`
- `Metrics.csv`

But `SKILL.md` Procedure defines **five narrative sections**:

1. Inventory the datastore
2. Profile account coverage
3. Profile activity coverage
4. Profile cash and income history
5. Profile derived data quality

The script covers a subset of section 1 quantitatively. I wrote sections 2–5 by querying canonical CSVs myself and synthesizing markdown. That is a large agent burden relative to Hello World.

**4. Evaluation skills are scaffolds, not deliverables**

`source-profile-insights` wrote a 3-line scorecard stub plus placeholder reflection text. `exit-interview` wrote question templates with "_Agent records verbatim Q&A here._"

I expanded both substantially to make the report useful. The overlay *procedure* says "run skills and merge into Report.md" — but the skills did not merge meaningful content.

**5. Inventory skill date-range bug**

`DataStoreInventory.csv` reported orders date range as 2026-06-14 → 2026-06-16 because the skill scans columns in order and picked `ExportedAtLocal` before `Date`. Ingestion manifest correctly showed 2024-06-24 → 2026-06-16. I cross-checked manually.

Trust erosion: when CSV output contradicts manifest, the agent must re-derive facts.

**6. Account coverage metrics are thin**

`AccountCoverage.csv` only includes `OrderRows` per account. The skill procedure asks for activity ranges, latest snapshots, gaps, and symmetry — none of which appear in the CSV. Again, agent fills the gap.

**7. Metrics.csv is minimal**

Two rows: `canonicalTableCount: 7`, `rawFileCount: 12`. Useful but far below what the five-section procedure implies. No cash confidence summary, dedup stats, or validation pass/fail flags.

**8. Analysis period defaults ambiguous**

User request: "execute the source profile playbook" — no period. I used full available range (20210827–20260616). Reasonable, but:

- README says *"Run a source profile for May 2026"*
- Contract says structured discovery should ask full range vs. subset
- Playbook manifest has no defaults for period inputs

**9. `knowledge/` tree is undocumented in pack contracts**

User datastore includes `knowledge/` (holdings, themes, theses, policies, etc.). Pack `user-datastore-layout.md` lists only `data/`, `reports/`, `inputs/`. PortfolioCoach README mentions knowledge under a `data/knowledge/` path that does not match on-disk layout either.

An execution agent cannot tell whether knowledge files are in scope for source-profile. I ignored them — probably correct — but authoring should say so explicitly.

**10. Exit interview without user present**

The skill expects Q&A with the user. In fire-and-forget test execution, I left "User responses pending" and added preliminary agent observations. The skill does not define behavior for async/unattended runs.

**11. No post-run validation**

Report folder had required artifacts, but nothing verified:

- All contract files present
- Path matches template tokens
- CSV row counts consistent with narrative

I self-checked.

**12. Pack README vs. execution authority**

Distribution README is good for discovery ("Try it" examples). Execution relied on manifests and contracts — correct per APP. But the gap between README promise (*"datastore inventory and quality review"*) and script deliverables (*CSV indexes + agent narrative*) is larger than Hello World.

---

### Portfolio-coach execution summary (what actually happened)

| Step | Planned | Actual |
| --- | --- | --- |
| Bind userDatastore | `UserData/jclark/PortfolioCoach` | Done |
| Merge workflow | Hash, merge, rebuild canonical | Validated existing state; no new attachments; no rebuild |
| Input discovery | Resolve period + evaluation | Defaults: full range, evaluation true |
| Core skill | `datastore-inventory` | Script ran; CSVs produced |
| Evaluation overlay | insights + exit-interview | Scaffolds produced; agent expanded |
| Report | Per contract | Agent-authored `Report.md` (~120 lines) + copied CSVs |
| Layout fix | None expected | Required `data/` junctions |

Output: `UserData/jclark/PortfolioCoach/reports/20260628-080448-SourceProfile-20210827-20260616/`

---

### Portfolio-coach authoring recommendations (prioritized)

| Priority | Recommendation |
| --- | --- |
| Critical | Fix **datastore path resolution** in `pc-lib` or enforce layout at validation |
| High | Implement **merge/rebuild skill** or narrow workflow scope to match shipped tooling |
| High | Expand `datastore-inventory` to emit **report section fragments** or structured JSON for sections 1–5 |
| High | Fix **date column selection** in inventory skill (prefer domain-specific columns per table) |
| High | Declare **analysis period default policy** in playbook or workflow |
| Medium | Enrich `AccountCoverage.csv` and `Metrics.csv` to match skill procedure |
| Medium | Upgrade `source-profile-insights` from scaffold to quantitative scorecard |
| Medium | Document **`knowledge/` out of scope** for source-profile (or add inputs if in scope) |
| Medium | Define **unattended exit-interview** behavior (skip, defer, or agent-only reflection) |
| Lower | Add optional `validate-report-folder.py` against `report-artifact-contract.md` |

---

### Bottom line on portfolio-coach

PortfolioCoach demonstrates that APP scales to real domain complexity in *specification* — contracts and playbook composition are strong. It also demonstrates where the POC breaks in *execution closure*:

- The written merge contract exceeds shipped scripts
- The skill procedure exceeds script outputs
- User datastore layout does not match tooling assumptions
- Evaluation overlay skills produce templates, not evaluation

Hello World proves APP works. PortfolioCoach proves domain packs need either **more script** or **honest scoping** so agents are not implicitly responsible for half the playbook. The contracts are production-quality prose; the executable surface should catch up to match them.

---

## Cross-cutting comparison

| Dimension | APP standard | Hello World | PortfolioCoach |
| --- | --- | --- | --- |
| Clarity for execution agent | Good grammar; weak operational guide | Excellent | Good manifests; weak script coverage |
| Skill completeness | N/A | Complete core skill | Scaffold-heavy |
| Contract quality | Strong authoring standard | Minimal, sufficient | Exceptional domain contract |
| Layout enforcement | Defined but not validated at runtime | Trivial layout | Mismatch broke tooling |
| Agent synthesis burden | Should be explicit policy | Low | High |
| Proof of concept success | Yes | Definitive | Partial — valuable stress test |

If you iterate one thing first: align PortfolioCoach's **executable surface** (scripts + layout resolution + defaults) with the quality of its **written contracts**. Hello World already shows the target experience; PortfolioCoach shows how far domain packs can drift when scripts lag the spec.

