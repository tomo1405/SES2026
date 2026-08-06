python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pytest

from src_0106 import task_func

def test_task_func_valid_input():
    df = pd.DataFrame({'group': ['A', 'B', 'C'], 'date': ['2021-01-01', '2021-01-02', '2021-01-03'], 'value': [10, 20, 30]})
    heatmap_fig, pairplot_grid = task_func(df)
    assert isinstance(heatmap_fig, plt.Figure)
    assert isinstance(pairplot_grid, sns.PairGrid)

def test_task_func_empty_df():
    df = pd.DataFrame()
    with pytest.raises(ValueError) as e:
        task_func(df)
    assert str(e.value) == "DataFrame must be non-empty and contain 'group', 'date', and 'value' columns."

def test_task_func_missing_column():
    df = pd.DataFrame({'group': ['A', 'B', 'C'], 'date': ['2021-01-01', '2021-01-02', '2021-01-03']})
    with pytest.raises(ValueError) as e:
        task_func(df)
    assert str(e.value) == "DataFrame must be non-empty and contain 'group', 'date', and 'value' columns."

def test_task_func_non_datetime_column():
    df = pd.DataFrame({'group': ['A', 'B', 'C'], 'date': ['2021-01-01', '2021-01-02', '2021-01-03'], 'value': [10, 20, 30], 'non_datetime_col': ['a', 'b', 'c']})
    with pytest.raises(ValueError) as e:
        task_func(df)
    assert str(e.value) == "'date' column must be in datetime format."

def test_task_func_error():
    df = pd.DataFrame({'group': ['A', 'B', 'C'], 'date': ['2021-01-01', '2021-01-02', '2021-01-03'], 'value': [10, 20, '30']})
    with pytest.raises(ValueError) as e:
        task_func(df)
    assert str(e.value) == "An error occurred: could not convert string to float: '30'"