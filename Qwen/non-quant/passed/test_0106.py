import pytest
from src_0106 import task_func
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@pytest.fixture
def sample_df():
    data = {
        'group': ['A', 'A', 'B', 'B'],
        'date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04']),
        'value': [10, 20, 30, 40]
    }
    return pd.DataFrame(data)

def test_task_func_valid_input(sample_df):
    heatmap_fig, pairplot_grid = task_func(sample_df)
    assert isinstance(heatmap_fig, plt.Figure)
    assert isinstance(pairplot_grid, sns.axisgrid.PairGrid)

def test_task_func_empty_dataframe():
    empty_df = pd.DataFrame()
    with pytest.raises(ValueError, match="DataFrame must be non-empty and contain 'group', 'date', and 'value' columns."):
        task_func(empty_df)

def test_task_func_missing_columns(sample_df):
    missing_col_df = sample_df.drop(columns=['group'])
    with pytest.raises(ValueError, match="DataFrame must be non-empty and contain 'group', 'date', and 'value' columns."):
        task_func(missing_col_df)

def test_task_func_non_datetime_date_column(sample_df):
    sample_df['date'] = sample_df['date'].astype(str)
    with pytest.raises(ValueError, match="'date' column must be in datetime format."):
        task_func(sample_df)