import pandas as pd
import random
import pytest

# Constants
N_DATA_POINTS = 10000
MIN_VALUE = 0.0
MAX_VALUE = 10.0

def task_func(n_data_points=N_DATA_POINTS):
    if n_data_points == 0:
        return pd.DataFrame(columns=['Value'])
    
    data = [round(random.uniform(MIN_VALUE, MAX_VALUE), 3) for _ in range(n_data_points)]
    data_df = pd.DataFrame(data, columns=['Value'])

    return data_df

def test_task_func():
    # Test case 1: n_data_points = 0
    expected_output = pd.DataFrame(columns=['Value'])
    actual_output = task_func(0)
    assert actual_output.equals(expected_output)

    # Test case 2: n_data_points > 0
    n_data_points = 100
    data = [round(random.uniform(MIN_VALUE, MAX_VALUE), 3) for _ in range(n_data_points)]
    expected_output = pd.DataFrame(data, columns=['Value'])
    actual_output = task_func(n_data_points)
    assert actual_output.equals(expected_output)

if __name__ == "__main__":
    pytest.main()