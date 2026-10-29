'''Now we're finally at the model'''

from abc import ABC, abstractmethod
from typing import Any

import pandas as pd
from sklearn.linear_model import LogisticRegression


class Model(ABC):
    '''
    abstract parent class for models: train fits on the train set, predict returns probabilities
    private attributes are the ones with leading underscores e.g. self._features
    kwargs here used to pass anything required for the underlying model
    '''

    def __init__(self, features: list[str], target: str, **kwargs: Any):
        self._features = features
        self._target = target
        self._kwargs = kwargs  # any extra keyword arguments, collected into a dict, e.g. {"solver": "newton-cholesky"}
        self.model = self._build_model()

    @abstractmethod
    def _build_model(self) -> Any: 
        '''return the (unfitted) sklearn model, built with self._kwargs; every child must define this'''

    def train(self, df: pd.DataFrame) -> None:
        '''fit self.model on the feature and target columns of df'''
        self.model.fit(df[self._features], df[self._target])

    def predict(self, df: pd.DataFrame) -> pd.Series:
        '''return the predicted probability of the positive class (1) for each row of df'''
        probabilities = self.model.predict_proba(df[self._features])[:, 1]  # column 1 = P(target = 1)
        return pd.Series(probabilities, index=df.index, name="predictions")


class LogisticRegressionModel(Model):
    '''logistic regression; extra keyword arguments are passed straight to sklearn's LogisticRegression'''

    def _build_model(self) -> LogisticRegression:
        return LogisticRegression(**self._kwargs)  # ** unpacks the dict back into keyword arguments
