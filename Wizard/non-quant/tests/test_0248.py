python
import pandas as pd
import random
from sklearn.preprocessing import StandardScaler
import pytest

# Constants
N_DATA_POINTS = 5000
MIN_VALUE = 0.0
MAX_VALUE = 10.0

def task_func(n_data_points=5000, min_value=0.0, max_value=10.0):
    if max_value < min_value:
        raise ValueError()

    data = [round(random.uniform(min_value, max_value), 3) for _ in range(n_data_points)]
    data_df = pd.DataFrame(data, columns=['Value'])

    scaler = StandardScaler()
    normalized_data = scaler.fit_transform(data_df[['Value']])

    return pd.DataFrame(normalized_data, columns=['Normalized Value'])

def test_task_func():
    # Test case 1: n_data_points is not an integer
    with pytest.raises(TypeError):
        task_func(n_data_points='5000', min_value=0.0, max_value=10.0)

    # Test case 2: min_value is greater than max_value
    with pytest.raises(ValueError):
        task_func(n_data_points=5000, min_value=10.0, max_value=0.0)

    # Test case 3: n_data_points is less than 1
    with pytest.raises(ValueError):
        task_func(n_data_points=0, min_value=0.0, max_value=10.0)

    # Test case 4: n_data_points is greater than 10000
    with pytest.raises(ValueError):
        task_func(n_data_points=10001, min_value=0.0, max_value=10.0)

    # Test case 5: min_value is not a float
    with pytest.raises(TypeError):
        task_func(n_data_points=5000, min_value='0.0', max_value=10.0)

    # Test case 6: max_value is not a float
    with pytest.raises(TypeError):
        task_func(n_data_points=5000, min_value=0.0, max_value='10.0')

    # Test case 7: n_data_points is not a float
    with pytest.raises(TypeError):
        task_func(n_data_points='5000', min_value=0.0, max_value=10.0)

    # Test case 8: max_value is less than min_value
    with pytest.raises(ValueError):
        task_func(n_data_points=5000, min_value=10.0, max_value=0.0)

    # Test case 9: n_data_points is 5000, min_value is 0.0, max_value is 10.0
    result = task_func(n_data_points=5000, min_value=0.0, max_value=10.0)
    assert result.shape == (5000, 1)
    assert result['Normalized Value'].min() >= -1.0
    assert result['Normalized Value'].max() <= 1.0

    # Test case 10: n_data_points is 1000, min_value is 5.0, max_value is 15.0
    result = task_func(n_data_points=1000, min_value=5.0, max_value=15.0)
    assert result.shape == (1000, 1)
    assert result['Normalized Value'].min() >= -1.0
    assert result['Normalized Value'].max() <= 1.0

    # Test case 11: n_data_points is 1, min_value is 0.0, max_value is 10.0
    result = task_func(n_data_points=1, min_value=0.0, max_value=10.0)
    assert result.shape == (1, 1)
    assert result['Normalized Value'].min() >= -1.0
    assert result['Normalized Value'].max() <= 1.0

    # Test case 12: n_data_points is 10000, min_value is 0.0, max_value is 10.0
    result = task_func(n_data_points=10000, min_value=0.0, max_value=10.0)
    assert result.shape == (10000, 1)
    assert result['Normalized Value'].min() >= -1.0
    assert result['Normalized Value'].max() <= 1.0