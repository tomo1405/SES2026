import pytest
from src_0102 import task_func
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

@pytest.fixture
def mock_data(monkeypatch):
    def mock_read_csv(url, sep, skiprows, header):
        # Create a mock DataFrame similar to the Boston dataset
        data = {
            'CRIM': [0.00632, 0.02731, 0.02729],
            'ZN': [18.0, 0.0, 0.0],
            'INDUS': [2.31, 7.07, 7.07],
            'CHAS': [0, 0, 0],
            'NOX': [0.538, 0.469, 0.469],
            'RM': [6.575, 6.421, 7.185],
            'AGE': [65.2, 78.9, 61.1],
            'DIS': [4.0900, 4.9671, 4.9671],
            'RAD': [1, 2, 2],
            'TAX': [296, 242, 242],
            'PTRATIO': [15.3, 17.8, 17.8],
            'B': [396.90, 396.90, 392.83],
            'LSTAT': [4.98, 9.14, 4.03]
        }
        return pd.DataFrame(data)

    monkeypatch.setattr(pd, 'read_csv', mock_read_csv)

def test_task_func(mock_data):
    ax = task_func()
    assert isinstance(ax, plt.Axes)
    # Check if the DataFrame has the correct columns
    df = ax.get_figure().get_axes()[0].collections[0].get_array().get_array()
    assert len(df) == 169  # 13 columns * 13 columns (correlation matrix)
    # Check if the plot is a heatmap
    assert isinstance(ax, sns.axisgrid.heatmap)
    # Check if the plot has annotations
    assert ax.get_children()[0].get_text() != ''

def test_task_func_exception(monkeypatch):
    def mock_read_csv_exception(*args, **kwargs):
        raise Exception("Mocked exception")

    monkeypatch.setattr(pd, 'read_csv', mock_read_csv_exception)

    with pytest.raises(ValueError) as exc_info:
        task_func()
    assert "An error occurred: Mocked exception" in str(exc_info.value)