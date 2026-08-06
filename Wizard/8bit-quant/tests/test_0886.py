python
import pandas as pd
import pytest
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from src_0886 import task_func


@pytest.fixture
def sample_data():
    return pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [50, 60, 70, 80, 90], 'C': [900, 900, 900, 900, 900]})


def test_valid_input(sample_data):
    predictions, model = task_func(sample_data)
    assert predictions is not None
    assert model is not None


def test_invalid_input():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [50, 60, 70], 'C': [900, 900, 900]})
    predictions, model = task_func(df)
    assert predictions is None
    assert model is None


def test_non_numeric_data():
    df = pd.DataFrame({'A': [1, 2, 3, 'a', 5], 'B': [50, 60, 70, 80, 90], 'C': [900, 900, 900, 900, 900]})
    predictions, model = task_func(df)
    assert predictions is None
    assert model is None


def test_filtering():
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [50, 60, 70, 80, 90], 'C': [900, 900, 900, 900, 900]})
    predictions, model = task_func(df)
    assert predictions.shape == (2, )
    assert model is not None


def test_linear_regression(sample_data):
    predictions, model = task_func(sample_data)
    assert isinstance(model, LinearRegression)
    assert predictions.shape == (2, )