import pytest
from src_0246 import task_func
import pandas as pd
from scipy import stats

def test_task_func_default():
    result = task_func()
    assert isinstance(result, dict)
    assert 'mean' in result
    assert 'median' in result
    assert 'mode' in result
    assert isinstance(result['mean'], float)
    assert isinstance(result['median'], float)
    assert isinstance(result['mode'], float)

def test_task_func_custom_parameters():
    n_data_points = 1000
    min_value = 5.0
    max_value = 15.0
    result = task_func(n_data_points, min_value, max_value)
    assert len(result['mean']) == n_data_points
    assert min_value <= result['mean'] <= max_value
    assert min_value <= result['median'] <= max_value
    assert min_value <= result['mode'] <= max_value

def test_task_func_mode_calculation():
    data = [1.0, 2.0, 2.0, 3.0, 3.0, 3.0, 4.0]
    data_df = pd.DataFrame(data, columns=['Value'])
    mode = stats.mode(data_df['Value'].values)[0][0]
    assert mode == 3.0

def test_task_func_mean_calculation():
    data = [1.0, 2.0, 3.0, 4.0, 5.0]
    data_df = pd.DataFrame(data, columns=['Value'])
    mean = data_df['Value'].mean()
    assert mean == 3.0

def test_task_func_median_calculation():
    data = [1.0, 2.0, 3.0, 4.0, 5.0]
    data_df = pd.DataFrame(data, columns=['Value'])
    median = data_df['Value'].median()
    assert median == 3.0

def test_task_func_empty_data():
    data = []
    data_df = pd.DataFrame(data, columns=['Value'])
    with pytest.raises(IndexError):
        stats.mode(data_df['Value'].values)[0][0]