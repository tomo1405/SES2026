import pytest
from src_0751 import task_func
import pandas as pd
import statsmodels.api as sm

# Mock data for testing
@pytest.fixture
def sample_df():
    data = {
        'target': [10, 20, 30, 40, 50],
        'feature1': [150, 160, 170, 180, 190],
        'feature2': [70, 80, 90, 100, 110]
    }
    return pd.DataFrame(data)

def test_task_func_with_empty_dataframe(sample_df):
    empty_df = pd.DataFrame()
    result = task_func(empty_df, 150, 80, ['target', 'feature1', 'feature2'])
    assert result is None

def test_task_func_with_no_matching_rows(sample_df):
    result = task_func(sample_df, 200, 60, ['target', 'feature1', 'feature2'])
    assert result is None

def test_task_func_with_valid_input(sample_df):
    result = task_func(sample_df, 150, 100, ['target', 'feature1', 'feature2'])
    assert isinstance(result, sm.regression.linear_model.RegressionResultsWrapper)

def test_task_func_with_invalid_column_names(sample_df):
    with pytest.raises(KeyError):
        task_func(sample_df, 150, 100, ['target', 'non_existent_feature', 'feature2'])

def test_task_func_with_single_row(sample_df):
    single_row_df = sample_df.iloc[[0]]
    result = task_func(single_row_df, 150, 80, ['target', 'feature1', 'feature2'])
    assert isinstance(result, sm.regression.linear_model.RegressionResultsWrapper)