import pytest
from src_0107 import task_func
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def test_task_func():
    # Test 1: Invalid input
    with pytest.raises(ValueError):
        task_func(pd.DataFrame())

    # Test 2: Valid input
    df = pd.DataFrame({'group': ['A', 'B', 'C'], 'date': ['2022-01-01', '2022-01-02', '2022-01-03'], 'value': [10, 20, 30]})
    model, y_pred, ax = task_func(df)
    assert isinstance(model, LinearRegression)
    assert isinstance(y_pred, pd.Series)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Value vs Date (Linear Regression Prediction)'
    assert ax.get_xlabel() == 'Date (ordinal)'
    assert ax.get_ylabel() == 'Value'
    assert len(ax.get_lines()) == 1
    assert len(ax.get_lines()[0].get_xdata()) == 3
    assert len(ax.get_lines()[0].get_ydata()) == 3