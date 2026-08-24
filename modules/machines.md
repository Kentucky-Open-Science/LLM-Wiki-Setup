# Module: machines — one brain, many hands

Enable when the user has more than one machine (or plans to). Single-machine
setups skip this entirely and lose nothing else.

## The architecture

Machines divide into **brains** (where agent sessions run) and **hands**
(reached over SSH to execute work). Common shapes, all supported:

- **Laptop brain, remote hands** — one coherent session on the laptop SSHes
  out to run/submit everything. Knowledge stays in one place.
- **Sessions on the workhorse** — agents run on an always-on workstation/GPU
  node (launched over SSH inside tmux/screen), steered from anywhere; the
  laptop is a viewing copy.
- **Mixed** — interactive sessions on the laptop, long-running ones on the
  workhorse. Most multi-machine users end here.

Interview (Wave 5) determines the shape by asking, per machine: does it run
agent sessions, with which harness, and does it need sessions that survive
disconnects?

## Remote steering — be honest per harness

- **Claude Code**: sessions can enable remote control and be steered from
  the Claude app on any device. Long-lived remote sessions: launch inside
  tmux/screen over SSH so they survive the SSH connection dropping.
- **Codex**: cloud tasks and IDE integration provide remote steering.
- **free-claude-code**: **no remote steering.** Design around it: sessions
  live in tmux/screen on the remote host; the user attaches over SSH (from
  a phone, a terminal app works). Say this plainly during setup.
- **Windows hosts**: no tmux natively — use WSL (recommended for
  remote-session hosting) or persistent Windows Terminal tabs; Windows
  ships an OpenSSH client and can run an OpenSSH server.

## Every machine is a wiki page

Each machine gets `wiki/machine-<name>.md` from `templates/machine-page.md`
(type definition: `types/machine.md`).
Infrastructure is knowledge, not configuration: the quirks, the guardrails,
the division of labor all live on the page with provenance, so they are
learned once and cited forever. Shared clusters and sensitive-data boxes
additionally get the guardrails module.

## SSH setup (per hand)

One `~/.ssh/config` block per machine (all three OSes; on Windows the file
is `C:\Users\<you>\.ssh\config` and the built-in OpenSSH client reads it):

```
Host <alias>
    HostName <host-or-ip>
    User <user>
    IdentityFile ~/.ssh/id_ed25519_<alias>
    IdentitiesOnly yes
    ServerAliveInterval 60
    ServerAliveCountMax 3
    # POSIX only — multiplexing reuses one auth for hours. OpenSSH on
    # Windows does not support ControlMaster; omit these three there.
    ControlMaster auto
    ControlPath ~/.ssh/cm-%r@%h-%p
    ControlPersist 4h
```

Key setup, then the verification the agent relies on:

```
ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519_<alias> -N ""
# copy the public key (POSIX: ssh-copy-id; Windows: append .pub to the
# remote's ~/.ssh/authorized_keys manually or via a one-line ssh command)
ssh -o BatchMode=yes <alias> hostname   # must succeed with no prompt
```

Record the tradeoff on the machine page: a no-passphrase key is what gives
the agent autonomy; anyone who can read the key file can connect. Acceptable
on a disk-encrypted personal machine; to harden, use a passphrase + agent
(macOS: `ssh-add --apple-use-keychain`; Windows: the `ssh-agent` service;
Linux: keychain/agent of choice).

Machines that cannot take a key (policy) use the password-file pattern in
`modules/cluster-guardrails.md` § secure box.

## Fanning out to viewing copies

When one machine is where work happens and another holds copies for the user
to browse (classic: headless workhorse + laptop), generate a small fan-out
step in the workhorse's instructions: after pushing, best-effort
`ssh <laptop-alias> "git -C <path> pull --ff-only"` for the wiki and the
repo just pushed. **A laptop that is asleep or off-network is normal, never
an error, and never retried in a loop** — it catches up next time. Large
non-git artifacts move only by explicit rsync/scp/robocopy for a task.

## Wiring hands to each other

If two hands share a network, give one key-based SSH to the other and record
reachability (both directions? which has the key?) on both machine pages.
This lets the brain orchestrate direct machine-to-machine transfers instead
of routing data through itself.
