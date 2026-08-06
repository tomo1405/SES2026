import pandas as pd
import pytest
from src_0880 import task_func


def test_empty_dataframe():
    data = pd.DataFrame()
    col1 = "col1"
    col2 = "col2"
    with pytest.raises(ValueError):
        task_func(data, col1, col2)

def test_non_existent_columns():
    data = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
    col1 = "col3"
    col2 = "col4"
    with pytest.raises(ValueError):
        task_func(data, col1, col2)

def test_non_categorical_data():
    data = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
    col1 = "col1"
    col2 = "col2"
    with pytest.raises(TypeError):
        task_func(data, col1, col2)

def test_single_category():
    data = pd.DataFrame({"col1": [1, 1, 1], "col2": [2, 2, 2]})
    col1 = "col1"
    col2 = "col2"
    with pytest.raises(ValueError):
        task_func(data, col1, col2)

def test_small_counts():
    data = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
    col1 = "col1"
    col2 = "col2"
    with pytest.raises(ValueError):
        task_func(data, col1, col2)

def test_valid_input():
    data = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
    col1 = "col1"
    col2 = "col2"
    p = task_func(data, col1, col2)
    assert p > 0.05