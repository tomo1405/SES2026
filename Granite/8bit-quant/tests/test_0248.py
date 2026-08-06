import random

import pandas as pd
import pytest
from sklearn.preprocessing import StandardScaler
from src_0248 import task_func

# Constants
N_DATA_POINTS = 5000
MIN_VALUE = 0.0
MAX_VALUE = 10.0

def test_task_func_valid_input():
    """
    Test that task_func returns a valid DataFrame for valid input.
    """
    data = [round(random.uniform(MIN_VALUE, MAX_VALUE), 3) for _ in range(N_DATA_POINTS)]
    data_df = pd.DataFrame(data, columns=['Value'])

    scaler = StandardScaler()
    normalized_data = scaler.fit_transform(data_df[['Value']])

    expected_df = pd.DataFrame(normalized_data, columns=['Normalized Value'])
    actual_df = task_func(n_data_points=N_DATA_POINTS, min_value=MIN_VALUE, max_value=MAX_VALUE)

    assert actual_df.equals(expected_df)

def test_task_func_invalid_input():
    """
    Test that task_func raises a ValueError for invalid input.
    """
    with pytest.raises(ValueError):
        task_func(n_data_points=N_DATA_POINTS, min_value=MAX_VALUE, max_value=MIN_VALUE)