import pandas as pd
import random
from scipy import stats
from src_0246 import task_func
import pytest

@pytest.fixture
def setup():
    n_data_points = 5000
    min_value = 0.0
    max_value = 10.0
    data = [round(random.uniform(min_value, max_value), 3) for _ in range(n_data_points)]
    data_df = pd.DataFrame(data, columns=['Value'])
    return data_df

def test_task_func_output(setup):
    data_df = setup
    result = task_func(n_data_points=len(data_df), min_value=data_df['Value'].min(), max_value=data_df['Value'].max())
    assert isinstance(result, dict)
    assert 'mean' in result and 'median' in result and 'mode' in result

def test_task_func_mean(setup):
    data_df = setup
    result = task_func(n_data_points=len(data_df), min_value=data_df['Value'].min(), max_value=data_df['Value'].max())
    assert result['mean'] == data_df['Value'].mean()

def test_task_func_median(setup):
    data_df = setup
    result = task_func(n_data_points=len(data_df), min_value=data_df['Value'].min(), max_value=data_df['Value'].max())
    assert result['median'] == data_df['Value'].median()

def test_task_func_mode(setup):
    data_df = setup
    result = task_func(n_data_points=len(data_df), min_value=data_df['Value'].min(), max_value=data_df['Value'].max())
    mode_result = stats.mode(data_df['Value'].values)[0][0]
    assert result['mode'] == mode_result