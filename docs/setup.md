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
| `UserPromptSubmit` | Each message | Asks the tutor to checkpoint session state if the journal is 10+ minutes stale |
| `Stop` | After each reply, at most every 10 minutes | Commits and pushes |
| `SessionEnd` | Session closes | Commits and pushes |

Scripts live in `scripts/`; wiring is in `.claude/settings.json` (Claude Code). Other assistants have no hooks and follow the checkpoint and close steps in `AGENTS.md` instead. A hard power loss skips `SessionEnd`, so at most about 10 minutes of commits are at risk; files saved to disk survive regardless.

A local-only pre-commit guard (`.git/hooks/pre-commit` with a term list in `.git/info/`, neither pushed) blocks commits containing work-specific terms; a blocked autosave reports the offending lines. `local/` is git-ignored and holds machine-specific context that must never be committed.

`.gitattributes` forces LF line endings so hook scripts and labs run unchanged under bash and WSL.

## Pending

Yocto environment checks (disk space, host packages, first background build) run once WSL has been restarted.
