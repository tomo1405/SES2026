import pandas as pd
import random
from scipy import stats
import pytest

def task_func(n_data_points=5000, min_value=0.0, max_value=10.0):
    data = [round(random.uniform(min_value, max_value), 3) for _ in range(n_data_points)]
    data_df = pd.DataFrame(data, columns=['Value'])

    mean = data_df['Value'].mean()
    median = data_df['Value'].median()
    mode = stats.mode(data_df['Value'].values)[0][0]

    return {'mean': mean, 'median': median, 'mode': mode}

def test_task_func():
    n_data_points = 5000
    min_value = 0.0
    max_value = 10.0
    result = task_func(n_data_points, min_value, max_value)
    assert isinstance(result, dict)
    assert 'mean' in result and 'median' in result and 'mode' in result
    assert isinstance(result['mean'], float)
    assert isinstance(result['median'], float)
    assert isinstance(result['mode'], float)

def test_task_func_with_invalid_input():
    with pytest.raises(ValueError):
        task_func(n_data_points='invalid', min_value=0.0, max_value=10.0)
    with pytest.raises(ValueError):
        task_func(n_data_points=5000, min_value='invalid', max_value=10.0)
    with pytest.raises(ValueError):
        task_func(n_data_points=5000, min_value=0.0, max_value='invalid')