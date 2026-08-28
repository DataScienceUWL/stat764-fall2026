# Course notebooks

Handed out as we go. **Do not edit files in this folder** — copy them to
`../work/` first, or the next `git pull` will conflict with my updates.

## Meetings

| # | Date | Notebook | Topic |
|---:|---|---|---|
| 1 | Tue Sep 8 | `m01/m01_predict_this.ipynb` | What statistical learning is — *runs in your browser, no install needed* |
| 2 | Thu Sep 10 | `m02/m02_smallest_honest_pipeline.ipynb` | The smallest honest pipeline |
| 3 | Tue Sep 15 | `m03/m03_generalization_resampling.ipynb` | Generalization and resampling |
| 4 | Thu Sep 17 | `m04/m04_leakage_laboratory.ipynb` | The leakage laboratory |

## Labs

Individual work, due **11:59 pm on the Tuesday after they are assigned**. Upload
the `.ipynb` to Canvas.

| Lab | Assigned | Due | Notebook |
|---|---|---|---|
| 1 | Tue Sep 8 | Tue Sep 15 | `labs/lab01/lab01.ipynb` |
| 2 | Tue Sep 15 | Tue Sep 22 | `labs/lab02/lab02.ipynb` |

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
