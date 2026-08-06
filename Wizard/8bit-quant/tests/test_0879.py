python
import pandas as pd
import pytest
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from src_0879 import task_func

def test_task_func():
    # Test case 1: Test with valid data
    data = {'col1': [1, 2, 3, 4, 5], 'col2': [6, 7, 8, 9, 10], 'col3': [11, 12, 13, 14, 15]}
    target = 'col2'
    test_size = 0.2
    random_state = 42
    expected_mse = 0.0
    expected_model = RandomForestRegressor(random_state=random_state)
    expected_data = pd.DataFrame(data)
    mse, model, data = task_func(data, target, test_size, random_state)
    assert mse == expected_mse
    assert model == expected_model
    assert data.equals(expected_data)

    # Test case 2: Test with empty data
    data = {}
    target = 'col2'
    test_size = 0.2
    random_state = 42
    with pytest.raises(ValueError):
        task_func(data, target, test_size, random_state)

    # Test case 3: Test with invalid target column
    data = {'col1': [1, 2, 3, 4, 5], 'col2': [6, 7, 8, 9, 10], 'col3': [11, 12, 13, 14, 15]}
    target = 'col4'
    test_size = 0.2
    random_state = 42
    with pytest.raises(ValueError):
        task_func(data, target, test_size, random_state)