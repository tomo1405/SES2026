import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pytest

from src_0106 import task_func

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        'group': ['A', 'B', 'C', 'D'],
        'date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04'],
        'value': [10, 20, 30, 40]
    })

def test_task_func_valid_input(sample_df):
    heatmap_fig, pairplot_grid = task_func(sample_df)
    assert isinstance(heatmap_fig, plt.Figure)
    assert isinstance(pairplot_grid, sns.PairGrid)

def test_task_func_invalid_input_empty_df(sample_df):
    sample_df = pd.DataFrame()
    with pytest.raises(ValueError) as exc_info:
        task_func(sample_df)
    assert "DataFrame must be non-empty" in str(exc_info.value)

def test_task_func_invalid_input_missing_columns(sample_df):
    sample_df = sample_df.drop(columns=['group'])
    with pytest.raises(ValueError) as exc_info:
        task_func(sample_df)
    assert "DataFrame must contain 'group', 'date', and 'value' columns" in str(exc_info.value)

def test_task_func_invalid_input_invalid_date_format(sample_df):
    sample_df['date'] = ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04']
    with pytest.raises(ValueError) as exc_info:
        task_func(sample_df)
    assert "'date' column must be in datetime format" in str(exc_info.value)

def test_task_func_exception_handling():
    with pytest.raises(ValueError) as exc_info:
        task_func(None)
    assert "An error occurred" in str(exc_info.value)