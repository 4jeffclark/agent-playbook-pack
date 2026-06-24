# Hello World User Datastore Layout

Bind `userDatastore` to a host directory. Use this structure beneath it:

```text
{userDatastore}/
  runs/       # immutable run output folders (reports and run manifests)
  inputs/     # optional user seed files (not required for hello-world)
```

Runs are append-only. Do not overwrite an existing run folder.
