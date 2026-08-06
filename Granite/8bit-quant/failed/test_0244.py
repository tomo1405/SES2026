import pandas as pd
import random
import pytest
from src_0244 import task_func

# Constants
N_DATA_POINTS = 10000
MIN_VALUE = 0.0
MAX_VALUE = 10.0

def test_task_func_with_zero_data_points():
    expected_df = pd.DataFrame(columns=['Value'])
    actual_df = task_func(0)
    assert expected_df.equals(actual_df)

def test_task_func_with_positive_data_points():
    n_data_points = random.randint(1, N_DATA_POINTS)
    data = [round(random.uniform(MIN_VALUE, MAX_VALUE), 3) for _ in range(n_data_points)]
    expected_df = pd.DataFrame(data, columns=['Value'])
    actual_df = task_func(n_data_points)
    assert expected_df.equals(actual_df)

def test_task_func_with_negative_data_points():
    with pytest.raises(ValueError):
        task_func(-1)

def test_task_func_with_invalid_data_points():
    with pytest.raises(TypeError):
        task_func('invalid')