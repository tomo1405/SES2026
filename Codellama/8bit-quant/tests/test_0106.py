import pytest
from src_0106 import task_func
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def test_task_func_empty_df():
    df = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(df)

def test_task_func_missing_columns():
    df = pd.DataFrame({'group': [1, 2, 3], 'date': [1, 2, 3], 'value': [1, 2, 3]})
    with pytest.raises(ValueError):
        task_func(df)

def test_task_func_invalid_date_format():
    df = pd.DataFrame({'group': [1, 2, 3], 'date': ['a', 'b', 'c'], 'value': [1, 2, 3]})
    with pytest.raises(ValueError):
        task_func(df)

def test_task_func_valid_input():
    df = pd.DataFrame({'group': [1, 2, 3], 'date': [1, 2, 3], 'value': [1, 2, 3]})
    heatmap_fig, pairplot_grid = task_func(df)
    assert isinstance(heatmap_fig, plt.Figure)
    assert isinstance(pairplot_grid, sns.PairGrid)