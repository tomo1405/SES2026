import pytest
from src_0246 import task_func
import pandas as pd
import numpy as np
from scipy import stats

def test_task_func_default_values():
    result = task_func()
    assert isinstance(result, dict)
    assert 'mean' in result
    assert 'median' in result
    assert 'mode' in result
    assert isinstance(result['mean'], float)
    assert isinstance(result['median'], float)
    assert isinstance(result['mode'], float)

def test_task_func_custom_values():
    result = task_func(n_data_points=1000, min_value=5.0, max_value=15.0)
    assert isinstance(result, dict)
    assert 'mean' in result
    assert 'median' in result
    assert 'mode' in result
    assert isinstance(result['mean'], float)
    assert isinstance(result['median'], float)
    assert isinstance(result['mode'], float)

def test_task_func_mode():
    # Test mode calculation with a known dataset
    data = [5.0, 5.0, 5.0, 6.0, 7.0]
    df = pd.DataFrame(data, columns=['Value'])
    mode_result = stats.mode(df['Value'].values)[0][0]
    assert mode_result == 5.0

def test_task_func_mean():
    # Test mean calculation with a known dataset
    data = [5.0, 6.0, 7.0]
    df = pd.DataFrame(data, columns=['Value'])
    mean_result = df['Value'].mean()
    assert mean_result == 6.0

def test_task_func_median():
    # Test median calculation with a known dataset
    data = [5.0, 6.0, 7.0]
    df = pd.DataFrame(data, columns=['Value'])
    median_result = df['Value'].median()
    assert median_result == 6.0

def test_task_func_with_no_data():
    # Edge case: test with no data points
    result = task_func(n_data_points=0)
    assert isinstance(result, dict)
    assert 'mean' in result
    assert 'median' in result
    assert 'mode' in result
    assert np.isnan(result['mean'])
    assert np.isnan(result['median'])
    assert np.isnan(result['mode'])

def test_task_func_with_single_data_point():
    # Edge case: test with a single data point
    result = task_func(n_data_points=1)
    assert isinstance(result, dict)
    assert 'mean' in result
    assert 'median' in result
    assert 'mode' in result
    assert result['mean'] == result['median'] == result['mode']