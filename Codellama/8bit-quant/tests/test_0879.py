import pandas as pd
import pytest
from src_0879 import task_func


def test_task_func_empty_data():
    data = pd.DataFrame()
    target = "target"
    test_size = 0.2
    random_state = None

    with pytest.raises(ValueError):
        task_func(data, target, test_size, random_state)

def test_task_func_invalid_target():
    data = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    target = "c"
    test_size = 0.2
    random_state = None

    with pytest.raises(ValueError):
        task_func(data, target, test_size, random_state)

def test_task_func_valid_data():
    data = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "target": [7, 8, 9]})
    target = "target"
    test_size = 0.2
    random_state = None

    mse, model, data = task_func(data, target, test_size, random_state)

    assert mse > 0
    assert isinstance(model, RandomForestRegressor)
    assert isinstance(data, pd.DataFrame)