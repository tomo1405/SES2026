import pytest
from src_0884 import task_func
import pandas as pd
from statsmodels.tsa.stattools import adfuller

# Mock the adfuller function to control its output
def mock_adfuller(series):
    # Return a p-value of 0.04 to simulate a stationary series
    return (0, 0.04, 0, 0, {}, {})

@pytest.fixture
def sample_df():
    data = {
        'column_a': [10, 20, 30, 40, 50],
        'column_b': [40, 50, 60, 70, 80],
        'column_c': [800, 900, 900, 900, 1000]
    }
    return pd.DataFrame(data)

def test_task_func_no_unique_values(sample_df):
    assert task_func(sample_df, 'column_a', 'column_b', 'column_c') == True

def test_task_func_empty_filtered_df(sample_df):
    # Modify the dataframe to make the filtered dataframe empty
    sample_df['column_b'] = [10, 20, 30, 40, 50]
    assert task_func(sample_df, 'column_a', 'column_b', 'column_c') == True

def test_task_func_stationary_series(sample_df, monkeypatch):
    # Patch the adfuller function to return a p-value of 0.04
    monkeypatch.setattr(statsmodels.tsa.stattools, 'adfuller', mock_adfuller)
    assert task_func(sample_df, 'column_a', 'column_b', 'column_c') == True

def test_task_func_non_stationary_series(sample_df, monkeypatch):
    # Patch the adfuller function to return a p-value of 0.06
    def mock_adfuller_non_stationary(series):
        return (0, 0.06, 0, 0, {}, {})
    monkeypatch.setattr(statsmodels.tsa.stattools, 'adfuller', mock_adfuller_non_stationary)
    assert task_func(sample_df, 'column_a', 'column_b', 'column_c') == False