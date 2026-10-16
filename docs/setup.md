# Setup

## Environment

| Tool | Role |
|---|---|
| Windows 11 + Git Bash | Host; Claude Code runs here |
| WSL Ubuntu 26.04 (distro `Ubuntu`) | Lab runtime: Python, C toolchain, Linux tooling, QEMU, Yocto |
| VS Code | Editor for all lab and project work |
| Claude Code | Tutor, run from this folder |

## Lab runtime (one time)

```bash
wsl.exe -d Ubuntu
python3 -m venv ~/.venvs/mastery
~/.venvs/mastery/bin/pip install pytest hypothesis mypy
```

The venv lives in the WSL home directory, not under `/mnt/c`, for speed.

Run a lab:

```bash
cd /mnt/c/Users/sundark/mastery
~/.venvs/mastery/bin/python -m pytest labs/<path>
```

## Editor

Open the folder with `code C:\Users\sundark\mastery`. For running and debugging labs inside Linux, use the WSL extension and select `~/.venvs/mastery/bin/python` as the interpreter.

## Remotes

`origin` fetches from GitHub and pushes to both private repos:

| Host | Repo |
|---|---|
| GitHub | `sundark1007/mastery` |
| GitLab | `ksundara.badboyz/mastery` |

Credentials are held by Git Credential Manager; remote URLs embed the account name so the personal accounts are used. Tokens are never stored in this repo.

## Automation

| Hook | Trigger | Action |
|---|---|---|
| `SessionStart` | Session opens | Records the session start time |
| `UserPromptSubmit` | Each message | Asks the tutor to checkpoint session state if the journal is 10+ minutes stale; injects the learner's response time |
| `Stop` | After each reply | Marks the reply time for the response timer; commits and pushes at most every 10 minutes |
| `SessionEnd` | Session closes | Commits and pushes |

Scripts live in `scripts/`; wiring is in `.claude/settings.json` (Claude Code). Other assistants have no hooks and follow the checkpoint and close steps in `AGENTS.md` instead. A hard power loss skips `SessionEnd`, so at most about 10 minutes of commits are at risk; files saved to disk survive regardless.

A local-only pre-commit guard (`.git/hooks/pre-commit` with a term list in `.git/info/`, neither pushed) blocks commits containing work-specific terms; a blocked autosave reports the offending lines. `local/` is git-ignored and holds machine-specific context that must never be committed.

`.gitattributes` forces LF line endings so hook scripts and labs run unchanged under bash and WSL.

## Yocto

Release 6.0 (wrynose, LTS), set up with `bitbake-setup` under `~/yocto` in WSL (Linux filesystem, not `/mnt/c`).

| Step | Command |
|---|---|
| Host packages and locale (one time, sudo) | `bash /mnt/c/Users/sundark/mastery/scripts/yocto/host-setup.sh` |
| Layers (one time) | `cd ~/yocto && ./bitbake/bin/bitbake-setup init --non-interactive poky-wrynose poky distro/poky machine/qemux86-64` |
| Build | `bash /mnt/c/Users/sundark/mastery/scripts/yocto/build.sh [target]` |

`build.sh` strips Windows entries from `PATH` (BitBake's sanity checks reject them), caps parallelism at 8 threads because WSL has about 15 GB of RAM (`YOCTO_THREADS` overrides), and logs each build under `build/logs/`. First builds take hours; run them outside sessions.
