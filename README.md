# 21DM1004 Computing for Data Science - Homework 5

Group members: Vienna Donnelly, Xu Jiang

## Submission files

| File | What it covers |
|---|---|
| [`src/computing4dc_hw5/hw5.py`](src/computing4dc_hw5/hw5.py) | Step 5: the exercises — `Patient` (Q1), `Card` and `Deck` (Q2), and the `PlaneFigure` interface with `Triangle`, `Rectangle` and `Circle` (Q3) |
| [`Diabetes.ipynb`](Diabetes.ipynb) | Step 7: imports the library's classes and runs the full process — load, preprocess, create features, train, predict on the test set, add the `predictions` column and compute the ROC AUC (plus an ROC curve) |

The notebook uses the library in `src/computing4dc_hw5/` (step 6):

| Module | Classes | Step |
|---|---|---|
| `toolkit.py` | `DataLoader` (load and split into train/test); `Preprocessor` interface with `DropMissingRows` and `FillWithMean` | 6a–c |
| `engineering.py` | `Feature` abstract parent class with `LogTransform`, `Square` and `OneHotEncode` | 6d |
| `model.py` | `Model` abstract parent class with `LogisticRegressionModel` (`train` and `predict`) | 6e–f |

`workings/` contains scratch notebooks from development and can be ignored.
