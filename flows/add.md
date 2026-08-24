# Flow: add — register a machine, repo, or collaborator

Targeted extensions for the three things that recur after setup. Each ends:
update `index.md`, log entry, commit (push if remote), and — when the
global device table or authorizations changed — regenerate + redeploy the
affected instruction files.

## add machine

1. Interview: name/alias, role (laptop / workstation / GPU node / shared
   cluster / secure box), ownership, who else uses it, what's at stake.
   Does it run agent sessions (which harness — remote-steerable per
   `modules/machines.md`?) or is it a hand reached over SSH?
2. Connection: SSH config block per `modules/machines.md` (OS-appropriate);
   key setup, or the secure-box password-file pattern
   (`modules/cluster-guardrails.md`) where keys are not allowed. Verify:
   `ssh -o BatchMode=yes <alias> hostname` — with the user's permission,
   this is the one remote action in the flow.
3. Guardrails: shared or sensitive ⇒ walk the cluster-guardrails interview
   questions; personal ⇒ at minimum "what on this machine is not
   expendable".
4. Page: `wiki/machine-<name>.md` from `templates/machine-page.md` — facts
   verified or conv-tagged, never invented. Link sibling machines
   (division of labor) and the projects that will run here.
5. Ripple: device table in `config/global.md` → regenerate → redeploy.
   If the wiki has a remote and the machine will host sessions: clone the
   wiki there; deploy the global file for that machine's harness.

## add repo

1. Locate it; read README + manifests; determine solo vs collaborative
   (P4 heuristic: authors in history vs the user's identities) and confirm.
2. Normalize per `modules/github-sync.md` (policy P2/P4 as configured):
   gitignore block (tailored), size-guard hook, remote + default branch
   confirmed.
3. Page: `wiki/project-<slug>.md` per the project type definition —
   purpose, structure, location, stack, relationships, provenance-tagged.
4. Per-repo instruction files if the user wants them for this repo (P6):
   generate from `templates/repo-instructions.md`; commit in solo repos;
   in collaborative ones, leave for the user to propose.
5. If the repo implies new activities (first LaTeX project; first
   pipeline), offer the matching catalog types — one line, per the lean
   rule.

## add collaborator

1. Interview: name, role, affiliation, what they own/build, which shared
   repos and machines they touch.
2. Page: `wiki/entity-<name-slug>.md` (person shape).
3. Ripple — the important one: repos where this person will commit become
   **collaborative** under P4 (pushes need approval). Update those repos'
   instruction files' declared status, and note the change to the user
   plainly.
