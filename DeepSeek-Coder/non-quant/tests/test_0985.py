import pytest
from src_0985 import task_func
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

@pytest.fixture
def sample_data():
    data = {
        'x': [1, 2, 3, 4, 5],
        'y': [2, 3, 5, 7, 11]
    }
    df = pd.DataFrame(data)
    return df

def test_task_func(sample_data):
    df = sample_data
    x_column = 'x'
    y_column = 'y'
    ax = task_func(df, x_column, y_column)

    assert ax is not None
    assert isinstance(ax, plt.Axes)

    # Add more assertions to check the plot if necessary