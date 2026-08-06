import pandas as pd
import random
from sklearn.preprocessing import StandardScaler
from src_0248 import task_func
import pytest

# Constants
N_DATA_POINTS = 5000
MIN_VALUE = 0.0
MAX_VALUE = 10.0

def test_task_func():
    # Test case 1: Normal input
    data = [round(random.uniform(MIN_VALUE, MAX_VALUE), 3) for _ in range(N_DATA_POINTS)]
    data_df = pd.DataFrame(data, columns=['Value'])
    expected_output = pd.DataFrame(StandardScaler().fit_transform(data_df[['Value']]), columns=['Normalized Value'])
    actual_output = task_func(n_data_points=N_DATA_POINTS, min_value=MIN_VALUE, max_value=MAX_VALUE)
    assert actual_output.equals(expected_output)

    # Test case 2: Invalid input (max_value < min_value)
    with pytest.raises(ValueError):
        task_func(n_data_points=N_DATA_POINTS, min_value=MAX_VALUE, max_value=MIN_VALUE)