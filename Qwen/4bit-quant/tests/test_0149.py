import pytest
from src_0149 import task_func
import pandas as pd

@pytest.fixture
def sample_df():
    data = {'category': ['A', 'B', 'A', 'C', 'B']}
    return pd.DataFrame(data)

def test_task_func(sample_df):
    result_df = task_func(sample_df, 'category')
    assert 'category' in result_df.columns, "The column 'category' should still be in the DataFrame"
    assert result_df['category'].dtype == int, "The 'category' column should be of integer type after encoding"
    assert set(result_df['category']) == {0, 1, 2}, "The encoded values should be integers starting from 0"

def test_task_func_with_empty_column(sample_df):
    sample_df['category'] = []
    result_df = task_func(sample_df, 'category')
    assert result_df['category'].isnull().all(), "All values in the 'category' column should be NaN if it was empty"

def test_task_func_with_single_value_column(sample_df):
    sample_df['category'] = ['A', 'A', 'A', 'A', 'A']
    result_df = task_func(sample_df, 'category')
    assert result_df['category'].unique().size == 1, "There should be only one unique value in the 'category' column"
    assert result_df['category'].iloc[0] == 0, "The encoded value should be 0 for a single category"

def test_task_func_with_non_existent_column(sample_df):
    with pytest.raises(KeyError):
        task_func(sample_df, 'non_existent_column')

def test_task_func_with_numeric_column(sample_df):
    sample_df['numeric'] = [1, 2, 3, 4, 5]
    result_df = task_func(sample_df, 'numeric')
    assert result_df['numeric'].equals(sample_df['numeric']), "The 'numeric' column should remain unchanged"