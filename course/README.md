# Course notebooks

Handed out as we go. **Do not edit files in this folder** — copy them to
`../work/` first, or the next `git pull` will conflict with my updates.

## Meetings

| # | Date | Notebook | Topic |
|---:|---|---|---|
| 1 | Tue Sep 8 | `Day01_090826/day01_predict_this.ipynb` | What statistical learning is — *runs in your browser, no install needed* |
| 2 | Thu Sep 10 | `Day02_091026/day02_smallest_honest_pipeline.ipynb` | The smallest honest pipeline |
| 3 | Tue Sep 15 | `Day03_091526/day03_generalization_resampling.ipynb` | Generalization and resampling |
| 4 | Thu Sep 17 | `Day04_091726/day04_leakage_laboratory.ipynb` | The leakage laboratory |
| 5 | Tue Sep 22 | `Day05_092226/day05_regression_as_prediction.ipynb` | Regression as prediction |
| 6 | Thu Sep 24 | `Day06_092426/day06_model_comparison_cv.ipynb` | Model comparison by cross-validation |

## Labs

Individual work, due **11:59 pm on the Tuesday after they are assigned**. Upload
the `.ipynb` to Canvas.

| Lab | Assigned | Due | Notebook |
|---|---|---|---|
| 1 | Tue Sep 8 | Tue Sep 15 | `labs/lab01/lab01.ipynb` |
| 2 | Tue Sep 15 | Tue Sep 22 | `labs/lab02/lab02.ipynb` |

## Reference notebooks

Not meetings, and nothing here is assessed. These are the longer arguments and
derivations that do not fit in a twenty-minute concept block. Read one when the short
version in class was not enough.

| Notebook | What it is |
|---|---|
| `reference/ref_sklearn_structures.ipynb` | **How scikit-learn is put together** — estimators, the trailing-underscore convention, `Pipeline`, `ColumnTransformer`. Start here if the pipeline in Meeting 2 felt like syntax you copied rather than code you understood. |
| `reference/ref_exploring_ames.ipynb` | **Exploring the Ames data** — a tool, not a reading. Almost every cell has a column name in it you are meant to change. Also: why you explore the *training* half. |
| `reference/ref_day03_studio.ipynb` | A reference implementation of the Day 3 studio — two contender sets through identical code, showing why some teams could flip their worst model in seconds and others could not flip it in 300 tries. |
| `reference/ref_day02_studio.ipynb` | A reference implementation of the Day 2 studio, with five things to check your own notebook against. |
| `reference/ref_coefficients_are_not_effects.ipynb` | What a regression coefficient actually tells you — the full argument behind "this course mostly declines explanation". |
| `reference/ref_boosting_from_scratch.ipynb` | Gradient boosting in six lines, checked against the library. Meeting 17 sends you here. |

A studio reference appears here after that studio has run.

## Data

`data/` holds every dataset the course uses, vendored so nothing depends on a
website being up during class.

| File | Rows | What it is |
|---|---:|---|
| `ames.csv` | 2,930 | Ames, Iowa home sales 2006–2010 (De Cock 2011). The recurring regression dataset. |
| `ames_day1*.csv` | 120 / 250 | The Meeting 1 split, with the answer key |
| `bike_hour.csv` | 17,379 | Capital Bikeshare hourly rentals 2011–2012 (UCI 275) |

## `stat764.py`

Shared helpers, so paths work the same from `course/` and from your copy in
`work/`:

```python
from stat764 import load
ames = load("ames.csv")
```

Every notebook opens with the four lines that make this importable. It is a plain
Python module rather than a notebook on purpose — anything reused across meetings
belongs in a module, and we will talk about why.

## Bigger datasets

`diabetes_130.csv.gz` and `county_health_*.csv.gz` are stored gzipped. Nothing
changes for you — `load("diabetes_130.csv")` finds the `.gz` and pandas reads it
directly.

| File | Rows | What it is |
|---|---:|---|
| `diabetes_130.csv.gz` | 101,766 | Diabetes 130-US Hospitals (UCI 296). **Encounters, not patients** — 71,518 patients, and 47,021 rows belong to someone with more than one visit. |
| `county_health_2025.csv.gz` | 3,204 | County Health Rankings 2025, ~790 columns. Week 11 (PCA). |
| `county_health_2024.csv.gz` | 3,195 | The 2024 release — a real held-out year. |

```python
from stat764 import diabetes
d = diabetes()                      # all 101,766 encounters
p = diabetes(patient_level=True)    # one row per patient, first encounter
```

## Capstone datasets

Too large or too multi-file to ship here. `fetch_data.py` downloads them:

```bash
python fetch_data.py --list     # what's available
python fetch_data.py --check    # are the sources still up?
python fetch_data.py loans      # download one
```

Three of them (OULAD, College Scorecard, FAA strikes) sit behind a form or
landing page and have to be downloaded by hand — `--list` marks those `[manual]`
and `--check` prints the page to get them from.
