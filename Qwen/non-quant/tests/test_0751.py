import pandas as pd
import pytest
from src_0751 import task_func


@pytest.fixture
def sample_df():
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50],
        'C': [50, 40, 30, 20, 10]
    }
    return pd.DataFrame(data)

def test_task_func_empty_df(sample_df):
    empty_df = pd.DataFrame()
    result = task_func(empty_df, 10, 50, ['A', 'B', 'C'])
    assert result is None

def test_task_func_no_matching_rows(sample_df):
    result = task_func(sample_df, 50, 10, ['A', 'B', 'C'])
    assert result is None

def test_task_func_valid_input(sample_df):
    result = task_func(sample_df, 10, 50, ['A', 'B', 'C'])
    assert isinstance(result, sm.regression.linear_model.RegressionResultsWrapper)

def test_task_func_invalid_columns(sample_df):
    with pytest.raises(KeyError):
        task_func(sample_df, 10, 50, ['A', 'D', 'C'])

def test_task_func_single_row(sample_df):
    single_row_df = sample_df.head(1)
    result = task_func(single_row_df, 10, 50, ['A', 'B', 'C'])
    assert isinstance(result, sm.regression.linear_model.RegressionResultsWrapper)

def test_task_func_all_rows(sample_df):
    result = task_func(sample_df, 5, 60, ['A', 'B', 'C'])
    assert isinstance(result, sm.regression.linear_model.RegressionResultsWrapper)