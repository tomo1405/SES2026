import pandas as pd
import numpy as np
from src_0175 import task_func

def test_task_func_valid_input():
    data = pd.DataFrame()
    key = 'random_key'
    min_value = 0
    max_value = 100
    result = task_func(data, key, min_value, max_value)
    assert isinstance(result, pd.DataFrame)
    assert key in result.columns
    assert (result[key] >= min_value).all()
    assert (result[key] <= max_value).all()

def test_task_func_invalid_input():
    data = 'not a DataFrame'
    key = 'random_key'
    min_value = 0
    max_value = 100
    with pytest.raises(ValueError) as exc_info:
        task_func(data, key, min_value, max_value)
    assert "Input 'data' must be a pandas DataFrame." in str(exc_info.value)

def test_task_func_invalid_type_input():
    data = pd.DataFrame()
    key = 123  # not a string
    min_value = 0
    max_value = 100
    with pytest.raises(TypeError) as exc_info:
        task_func(data, key, min_value, max_value)
    assert "Input 'key' must be a string." in str(exc_info.value)

def test_task_func_invalid_value_input():
    data = pd.DataFrame()
    key = 'random_key'
    min_value = 'not an integer'  # not an integer
    max_value = 100
    with pytest.raises(TypeError) as exc_info:
        task_func(data, key, min_value, max_value)
    assert "Inputs 'min_value' and 'max_value' must be integers." in str(exc_info.value)