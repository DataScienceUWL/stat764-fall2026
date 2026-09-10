"""Verify the STAT 764 environment.  Run with:  uv run python check_setup.py"""
import sys

print(f"Python {sys.version.split()[0]}")
print(f"  at {sys.executable}\n")

need = ["numpy", "pandas", "matplotlib", "sklearn", "statsmodels", "ipykernel"]
missing = []
for name in need:
    try:
        mod = __import__(name)
        print(f"  ok   {name:<14} {getattr(mod, '__version__', '?')}")
    except ImportError:
        print(f"  MISSING  {name}")
        missing.append(name)

print()
if missing:
    print("Not ready. Missing:", ", ".join(missing))
    print("Try:  uv sync")
    print("If that doesn't fix it, bring it to class -- don't lose an evening.")
    sys.exit(1)

if ".venv" not in sys.executable:
    print("Packages found, but you may be running the wrong Python.")
    print("Expected an interpreter inside .venv -- check your VS Code kernel.")
    sys.exit(1)

print("All good. You're ready for class.\n")

# The check above ran in the terminal, where `uv run` always picks the right
# Python. VS Code is a separate question: it has to FIND this interpreter.
print("-" * 62)
print("If VS Code cannot find the kernel, this is the path it wants:\n")
print(f"    {sys.executable}\n")
print("  1. Make sure VS Code has the FOLDER open, not just the notebook:")
print("     File > Open Folder > stat764-fall2026")
print("  2. Click 'Select Kernel' (top right of the notebook)")
print("       > Select Another Kernel... > Python Environments... > .venv")
print("  3. Still not listed? Cmd+Shift+P (Ctrl+Shift+P on Windows),")
print("     'Python: Select Interpreter', 'Enter interpreter path...',")
print("     and paste the path printed above. That always works.")
print("-" * 62)
