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

RAW = ("https://raw.githubusercontent.com/DataScienceUWL/stat764-fall2026/"
       "main/course/data/")


def repo_root(start: pathlib.Path | None = None) -> pathlib.Path:
    """The stat764-fall2026 directory, found by walking up from `start`."""
    here = (start or pathlib.Path.cwd()).resolve()
    for p in [here, *here.parents]:
        if (p / "course" / "stat764.py").exists():
            return p
    # Not above us. Maybe we are sitting just *outside* the clone -- a very
    # common way to get here is opening the parent folder in VS Code.
    for depth in (1, 2):
        for cand in here.glob("/".join(["*"] * depth) + "/course/stat764.py"):
            return cand.parent.parent
    raise FileNotFoundError(
        "Could not find your clone of stat764-fall2026.\n"
        f"  You are in: {here}\n"
        "  In VS Code, use File > Open Folder and choose the stat764-fall2026\n"
        "  folder itself -- not its parent, and not work/.\n"
        "  (Running in Colab? That is fine -- load() falls back to GitHub.)"
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
    """Read a course dataset by filename: load('ames.csv').

    Reads the local copy in course/data/ when there is one. If the repo cannot
    be found -- in Colab, or from a notebook saved outside the clone -- falls
    back to reading the same file over the network, so the notebook still runs.
    """
    try:
        return pd.read_csv(data_path(name), **kwargs)
    except FileNotFoundError:
        for candidate in (name, f"{name}.gz"):
            try:
                df = pd.read_csv(RAW + candidate, **kwargs)
                print(f"  (no local copy — read {candidate} from GitHub)")
                return df
            except Exception:
                continue
        raise


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
