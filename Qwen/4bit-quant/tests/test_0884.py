import pytest
from src_0884 import task_func
import pandas as pd

@pytest.fixture
def sample_df():
    data = {
        'column_a': [10, 20, 30, 40, 50],
        'column_b': [60, 70, 80, 90, 100],
        'column_c': [900, 900, 900, 900, 900]
    }
    return pd.DataFrame(data)

def test_task_func_no_unique_values(sample_df):
    assert task_func(sample_df, 'column_a', 'column_b', 'column_c') == True

def test_task_func_empty_filtered_df(sample_df):
    sample_df['column_b'] = [40, 40, 40, 40, 40]
    assert task_func(sample_df, 'column_a', 'column_b', 'column_c') == True

def test_task_func_adf_test_pass(sample_df):
    # Mocking the adfuller result to simulate p-value <= 0.05
    def mock_adfuller(series):
        return (0.0, 0.04, None, None, None, None)
    
    adfuller = mock_adfuller
    assert task_func(sample_df, 'column_a', 'column_b', 'column_c') == True

def test_task_func_adf_test_fail(sample_df):
    # Mocking the adfuller result to simulate p-value > 0.05
    def mock_adfuller(series):
        return (0.0, 0.06, None, None, None, None)
    
    adfuller = mock_adfuller
    assert task_func(sample_df, 'column_a', 'column_b', 'column_c') == False