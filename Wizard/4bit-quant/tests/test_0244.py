python
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
    data_df = task_func(0)
    assert data_df.shape == (0, 1)

    # Test case 2: n_data_points = 10000
    data_df = task_func(10000)
    assert data_df.shape == (10000, 1)
    assert data_df['Value'].min() >= MIN_VALUE
    assert data_df['Value'].max() <= MAX_VALUE
    assert data_df['Value'].apply(lambda x: isinstance(x, float)).all()