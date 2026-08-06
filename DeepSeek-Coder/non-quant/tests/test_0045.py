import pytest
from src_0045 import task_func
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

@pytest.fixture
def sample_data():
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1],
        'C': [2, 3, 4, 5, 6]
    }
    return pd.DataFrame(data)

def test_task_func(sample_data):
    df = sample_data
    result = task_func(df)
    assert isinstance(result, tuple), "The function should return a tuple."
    df, ax = result
    assert isinstance(df, pd.DataFrame), "The first element of the tuple should be a DataFrame."
    assert isinstance(ax, plt.Axes), "The second element of the tuple should be a matplotlib Axes object."
    assert len(df.columns) > 0, "The DataFrame should not be empty."
    assert len(df.columns) == 3, "The DataFrame should have the correct number of columns."