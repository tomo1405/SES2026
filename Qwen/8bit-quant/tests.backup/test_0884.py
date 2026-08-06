import pytest
from src_0884 import task_func
import pandas as pd
from statsmodels.tsa.stattools import adfuller

# Mocking the adfuller function to control its output
def mock_adfuller(series):
    return (1.0, 0.01, 2, 3, {'1%': -3.4319, '5%': -2.862, '10%': -2.567}, 150)

# Patching the adfuller function with the mock
adfuller = mock_adfuller

def test_task_func_single_unique_value():
    data = {
        'A': [10],
        'B': [60],
        'C': [900]
    }
    df = pd.DataFrame(data)
    result = task_func(df, 'A', 'B', 'C')
    assert result is True

def test_task_func_empty_dataframe():
    data = {
        'A': [],
        'B': [],
        'C': []
    }
    df = pd.DataFrame(data)
    result = task_func(df, 'A', 'B', 'C')
    assert result is True

def test_task_func_p_value_less_than_0_05():
    data = {
        'A': [10, 20, 30],
        'B': [60, 60, 60],
        'C': [900, 900, 900]
    }
    df = pd.DataFrame(data)
    result = task_func(df, 'A', 'B', 'C')
    assert result is True

def test_task_func_p_value_greater_than_0_05():
    # Adjust the mock_adfuller function to return a p-value greater than 0.05
    def mock_adfuller_high_p(series):
        return (1.0, 0.1, 2, 3, {'1%': -3.4319, '5%': -2.862, '10%': -2.567}, 150)
    
    global adfuller
    adfuller = mock_adfuller_high_p

    data = {
        'A': [10, 20, 30],
        'B': [60, 60, 60],
        'C': [900, 900, 900]
    }
    df = pd.DataFrame(data)
    result = task_func(df, 'A', 'B', 'C')
    assert result is False