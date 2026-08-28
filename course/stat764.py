"""Helpers shared across STAT 764 notebooks.

Anything reused across meetings lives here rather than being pasted into every
notebook. That split — the notebook carries the narrative, the module carries the
machinery — is a habit this course is trying to build, and it is the reason your
capstone will still run in December.

Notebooks reach this module with a four-line bootstrap that walks up from wherever
you opened them, so it works from `course/` and from your copy in `work/`.
"""

import pathlib

import pandas as pd


def repo_root(start: pathlib.Path | None = None) -> pathlib.Path:
    """The stat764-fall2026 directory, found by walking up from `start`."""
    here = (start or pathlib.Path.cwd()).resolve()
    for p in [here, *here.parents]:
        if (p / "course" / "stat764.py").exists():
            return p
    raise FileNotFoundError(
        "Could not find the course repo. Open this notebook from inside your "
        "clone of stat764-fall2026 (course/ or work/)."
    )


def data_path(name: str) -> pathlib.Path:
    """Absolute path to a file in course/data/."""
    p = repo_root() / "course" / "data" / name
    if not p.exists():
        have = sorted(q.name for q in p.parent.glob("*.csv"))
        raise FileNotFoundError(f"No course/data/{name}. Available: {', '.join(have)}")
    return p


def load(name: str, **kwargs) -> pd.DataFrame:
    """Read a course dataset by filename: load('ames.csv')."""
    return pd.read_csv(data_path(name), **kwargs)


def ames_day1() -> tuple[pd.DataFrame, pd.DataFrame, pd.Series]:
    """Meeting 1's split: (train, holdout_without_price, true_prices)."""
    train = load("ames_day1.csv")
    holdout = load("ames_day1_holdout.csv")
    key = load("ames_day1_key.csv").set_index("id")["SalePrice"]
    return train, holdout, key.loc[holdout["id"]]
