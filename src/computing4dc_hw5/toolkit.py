'''Classes in this module are used for data loading and preprocessing'''

from abc import ABC, abstractmethod
from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split

PACKAGE_DIR = Path(__file__).resolve().parent  # the folder this file is in: src/computing4dc_hw5
DATA_PATH = PACKAGE_DIR / "sample_diabetes_mellitus_data.csv"
TARGET = "diabetes_mellitus"
DROP_NA_COLUMNS = ["age", "gender", "ethnicity"]
FILL_MEAN_COLUMNS = ["height", "weight"]


class DataLoader:
    '''object to load csv data and split into train and test sets'''

    def __init__(
        self,
        data_path: Path = DATA_PATH,
        target: str = TARGET,
        test_size: float = 0.2,
        random_state: int | None = None,
    ):
        self.data_path = data_path
        self.target = target
        self.test_size = test_size
        self.random_state = random_state

    def get_data(self, index_col: str | None = None) -> tuple[pd.DataFrame, pd.DataFrame]:
        '''load csv data and split into train and test sets'''
        df = pd.read_csv(self.data_path, index_col=0)  # default index: the CSV's unnamed first column
        if index_col is not None:
            df = df.set_index(index_col)

        df_train, df_test = train_test_split(
            df,
            test_size=self.test_size,
            random_state=self.random_state,
            stratify=df[self.target],  # keeps the same diabetes rate in train and test
        )

        return df_train, df_test


class Preprocessor(ABC):
    '''abstract parent class (interface) for preprocessors: learn_from learns from train, transform changes a dataframe'''

    def learn_from(self, df: pd.DataFrame) -> Preprocessor:
        '''learn whatever the preprocessor needs from the train set; by default there's nothing to learn'''
        return self

    @abstractmethod
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        '''return a processed copy of df; every child must define this'''


class DropMissingRows(Preprocessor):
    '''removes rows that have NaN in any of the given columns'''

    def __init__(self, columns: list[str] = DROP_NA_COLUMNS):
        self.columns = columns

    # no learn_from here: dropping rows needs nothing from the train set, so the parent's is used

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        return df.dropna(subset=self.columns)


class FillWithMean(Preprocessor):
    '''fills NaN in the given columns with each column's mean, learned from the TRAIN set'''

    def __init__(self, columns: list[str] = FILL_MEAN_COLUMNS):
        self.columns = columns
        self.means = None  # set by learn_from

    def learn_from(self, df: pd.DataFrame) -> FillWithMean:
        self.means = df[self.columns].mean()  # remembered on the object until transform needs it
        return self

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        if self.means is None:
            raise RuntimeError("call learn_from() on the train set before transform()")
        return df.fillna(self.means)  # a Series of means fills each column with its own mean
