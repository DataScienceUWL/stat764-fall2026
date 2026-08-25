# STAT 764 — Statistical Learning · Fall 2026

Course notebooks and materials. UW–La Crosse, MS Applied Statistics.

**Canvas:** <https://uws.instructure.com/courses/869255>

---

## Getting the materials

Clone once:

```bash
git clone https://github.com/DataScienceUWL/stat764-fall2026.git
cd stat764-fall2026
```

Then **every Tuesday before class**, get that week's notebooks:

```bash
git pull
```

In VS Code you can click **Sync** in the Source Control panel instead — no terminal needed.

---

## The one rule

```
course/   ← notebooks I hand out.  NEVER EDIT THESE.
work/     ← copy a notebook here, then edit.  Yours, stays local.
```

**Copy before you edit.** If you edit a file in `course/`, the next `git pull` will
conflict with my updates and you'll lose time untangling it. Copy it to `work/` first
and that never happens.

Nothing you put in `work/` is uploaded anywhere — it's ignored by git and stays on your
machine.

---

## Setting up Python

Full instructions with screenshots are on Canvas:
**[Software Setup](https://uws.instructure.com/courses/869255/pages/software-setup)**

The short version:

```bash
# 1. Install uv  (macOS/Linux)
curl -LsSf https://astral.sh/uv/install.sh | sh
#    Windows PowerShell:
#    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# 2. Install VS Code from https://code.visualstudio.com/
#    Add the "Python" and "Jupyter" extensions (both by Microsoft)

# 3. From inside this folder, create the environment
uv sync

# 4. Check it worked
uv run python check_setup.py
```

Then open this folder in VS Code (**File → Open Folder**). When you open a notebook,
VS Code asks which kernel to use — **choose the one inside `.venv`**. That single step
is the most common thing to get wrong; if you see `ModuleNotFoundError` for a package
you just installed, you picked the wrong kernel.

**If something fails, stop and bring it to class.** Setup problems are common and have
nothing to do with your ability. We fix them together.

---

## Working habit: Restart & Run All

Before you submit anything, run **Kernel → Restart Kernel and Run All Cells**.

If it doesn't survive a clean restart, it isn't finished. Notebooks let you run cells
out of order and quietly accumulate state that exists only in memory — which is the
single most common way an analysis becomes irreproducible. We'll talk about this
properly, but the habit starts now.

---

## Submitting

Notebooks go to **Canvas**, not to git. Download or export from VS Code and upload to
the assignment.

---

## Layout

```
course/     weekly notebooks and data — read only
work/       your workspace — gitignored
pyproject.toml, uv.lock    the environment
check_setup.py             verifies your install
```
