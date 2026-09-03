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
    """Absolute path to a file in course/data/.

    Larger datasets are stored gzipped, so `data_path("diabetes_130.csv")` finds
    `diabetes_130.csv.gz`. pandas reads either transparently.
    """
    folder = repo_root() / "course" / "data"
    for candidate in (folder / name, folder / f"{name}.gz"):
        if candidate.exists():
            return candidate
    have = sorted(q.name for q in folder.glob("*.csv*"))
    raise FileNotFoundError(f"No course/data/{name}. Available: {', '.join(have)}")


def load(name: str, **kwargs) -> pd.DataFrame:
    """Read a course dataset by filename: load('ames.csv')."""
    return pd.read_csv(data_path(name), **kwargs)


def diabetes(patient_level: bool = False) -> pd.DataFrame:
    """Diabetes 130-US Hospitals (UCI 296). 101,766 encounters, 71,518 patients.

    Encounters, not patients — `patient_nbr` recurs. A random split puts the same
    patient on both sides. Pass patient_level=True for one row per patient (the
    first encounter), or keep every row and group on `patient_nbr` when splitting.
    """
    d = load("diabetes_130.csv", low_memory=False)
    if patient_level:
        d = d.sort_values("encounter_id").groupby("patient_nbr", as_index=False).first()
    return d


def ames_day1() -> tuple[pd.DataFrame, pd.DataFrame, pd.Series]:
    """Meeting 1's split: (train, holdout_without_price, true_prices)."""
    train = load("ames_day1.csv")
    holdout = load("ames_day1_holdout.csv")
    key = load("ames_day1_key.csv").set_index("id")["SalePrice"]
    return train, holdout, key.loc[holdout["id"]]
