python
import pandas as pd
import random
from sklearn.preprocessing import StandardScaler
import pytest

# Constants
N_DATA_POINTS = 5000
MIN_VALUE = 0.0
MAX_VALUE = 10.0

def task_func(n_data_points=N_DATA_POINTS, min_value=MIN_VALUE, max_value=MAX_VALUE):
    if max_value < min_value:
        raise ValueError()

    data = [round(random.uniform(min_value, max_value), 3) for _ in range(n_data_points)]
    data_df = pd.DataFrame(data, columns=['Value'])

    scaler = StandardScaler()
    normalized_data = scaler.fit_transform(data_df[['Value']])

    return pd.DataFrame(normalized_data, columns=['Normalized Value'])

def test_task_func():
    # Test case 1
    assert task_func().shape == (N_DATA_POINTS, 1)

    # Test case 2
    assert task_func(n_data_points=10000).shape == (10000, 1)

    # Test case 3
    assert task_func(min_value=5.0, max_value=15.0).shape == (N_DATA_POINTS, 1)

    # Test case 4
    with pytest.raises(ValueError):
        task_func(min_value=15.0, max_value=5.0)

    # Test case 5
    with pytest.raises(ValueError):
        task_func(min_value=15.0)

    # Test case 6
    with pytest.raises(ValueError):
        task_func(max_value=5.0)