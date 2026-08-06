import pandas as pd
import pytest
from src_0879 import task_func


def test_task_func():
    # Testing with valid data
    data = pd.DataFrame({'feature1': [1, 2, 3], 'feature2': [4, 5, 6], 'target': [7, 8, 9]})
    target = 'target'
    test_size = 0.2
    random_state = 42
    mse, model, data = task_func(data, target, test_size, random_state)
    assert mse > 0
    assert isinstance(model, RandomForestRegressor)
    assert isinstance(data, pd.DataFrame)

    # Testing with invalid data
    data = pd.DataFrame({'feature1': [1, 2, 3], 'feature2': [4, 5, 6], 'target': [7, 8, 9]})
    target = 'invalid_target'
    test_size = 0.2
    random_state = 42
    with pytest.raises(ValueError):
        task_func(data, target, test_size, random_state)

    # Testing with empty data
    data = pd.DataFrame({'feature1': [1, 2, 3], 'feature2': [4, 5, 6], 'target': [7, 8, 9]})
    target = 'target'
    test_size = 0.2
    random_state = 42
    with pytest.raises(ValueError):
        task_func(pd.DataFrame(), target, test_size, random_state)