import pytest
from src_0753 import task_func
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

def test_task_func_data_not_dataframe():
    data = "not a dataframe"
    target_column = "target"
    test_size = 0.2
    random_state = 0

    with pytest.raises(ValueError):
        task_func(data, target_column, test_size, random_state)

def test_task_func_data_empty():
    data = pd.DataFrame()
    target_column = "target"
    test_size = 0.2
    random_state = 0

    with pytest.raises(ValueError):
        task_func(data, target_column, test_size, random_state)

def test_task_func_target_column_not_in_data():
    data = pd.DataFrame({"feature1": [1, 2, 3], "feature2": [4, 5, 6]})
    target_column = "target"
    test_size = 0.2
    random_state = 0

    with pytest.raises(ValueError):
        task_func(data, target_column, test_size, random_state)

def test_task_func_data_values_not_numeric():
    data = pd.DataFrame({"feature1": ["a", "b", "c"], "feature2": [4, 5, 6]})
    target_column = "target"
    test_size = 0.2
    random_state = 0

    with pytest.raises(ValueError):
        task_func(data, target_column, test_size, random_state)

def test_task_func_test_size_invalid():
    data = pd.DataFrame({"feature1": [1, 2, 3], "feature2": [4, 5, 6]})
    target_column = "target"
    test_size = 1.5
    random_state = 0

    with pytest.raises(ValueError):
        task_func(data, target_column, test_size, random_state)

def test_task_func_random_state_not_integer():
    data = pd.DataFrame({"feature1": [1, 2, 3], "feature2": [4, 5, 6]})
    target_column = "target"
    test_size = 0.2
    random_state = "not an integer"

    with pytest.raises(ValueError):
        task_func(data, target_column, test_size, random_state)

def test_task_func_valid_input():
    data = pd.DataFrame({"feature1": [1, 2, 3], "feature2": [4, 5, 6]})
    target_column = "target"
    test_size = 0.2
    random_state = 0

    result = task_func(data, target_column, test_size, random_state)

    assert isinstance(result, float)
    assert result >= 0
    assert result <= 1