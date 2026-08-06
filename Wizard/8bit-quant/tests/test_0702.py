python
import pandas as pd
import pytest
from sklearn.linear_model import LinearRegression
from src_0702 import task_func

@pytest.fixture
def sample_data():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    target = 'A'
    return df, target

def test_task_func(sample_data):
    df, target = sample_data
    X = pd.DataFrame.drop(df, target, axis=1)
    y = pd.Series(df[target])

    model = LinearRegression()
    model.fit(X, y)

    assert task_func(df, target) == model.score(X, y)