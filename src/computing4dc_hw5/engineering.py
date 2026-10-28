'''Here, we are doing feature engineering'''

from abc import ABC, abstractmethod

import numpy as np
import pandas as pd


class Feature(ABC):
    '''abstract parent class for features: every feature adds new columns and keeps the original ones

    learn_from learns whatever the feature needs from the train set; transform returns a copy with the new columns
    '''

    def __init__(self, columns: list[str]):
        self.columns = columns

    def learn_from(self, df: pd.DataFrame) -> Feature:
        '''by default, there's nothing to learn'''
        return self

    @abstractmethod
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        '''return a copy of df with the new feature columns added; every child must define this'''


class LogTransform(Feature):
    '''adds log_<column> for each column (values must be positive)'''

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()  # work on a copy - good practice yeah
        for col in self.columns:
            df[f"log_{col}"] = np.log(df[col])
        return df


class Square(Feature):
    '''adds <column>_squared for each column'''

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        for col in self.columns:
            df[f"{col}_squared"] = df[col] ** 2
        return df


class OneHotEncode(Feature):
    '''adds a 0/1 column <column>_<category> for each category seen in the TRAIN set'''
    categories = None

    def learn_from(self, df: pd.DataFrame) -> OneHotEncode:
        # learning from train only means train and test get exactly the same new columns 
        # this avoids the problem of test having a category that train didn't have, which would cause errors in the model
        self.categories = {col: sorted(df[col].dropna().unique()) for col in self.columns}
        return self

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        if self.categories is None:
            raise RuntimeError("call learn_from() on the train set before transform()")
        df = df.copy()
        for col, categories in self.categories.items():
            for category in categories:
                df[f"{col}_{category}"] = (df[col] == category).astype(int)  # 1 where the row has this category
        return df
