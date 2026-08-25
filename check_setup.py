"""Verify the STAT 764 environment.  Run with:  uv run python check_setup.py"""
import sys

print(f"Python {sys.version.split()[0]}")
print(f"  at {sys.executable}\n")

need = ["numpy", "pandas", "matplotlib", "sklearn", "statsmodels"]
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

print("All good. You're ready for class.")
