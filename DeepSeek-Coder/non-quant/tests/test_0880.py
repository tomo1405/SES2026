import pytest
from src_0880 import task_func
import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

# Test cases for task_func

def test_task_func_empty_dataframe():
    data = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(data, "col1", "col2")

def test_task_func_missing_columns():
    data = pd.DataFrame({
        "col1": [1, 2, 3],
        "col2": [4, 5, 6]
    })
    with pytest.raises(ValueError):
        task_func(data, "col1", "col3")

def test_task_func_non_categorical_data():
    data = pd.DataFrame({
        "col1": [1, 2, 3],
        "col2": [4, 5, 6]
    })
    with pytest.raises(TypeError):
        task_func(data, "col1", "col2")

def test_task_func_single_category():
    data = pd.DataFrame({
        "col1": [1, 1, 1],
        "col2": [2, 2, 2]
    })
    with pytest.raises(ValueError):
        task_func(data, "col1", "col2")

def test_task_func_small_counts():
    data = pd.DataFrame({
        "col1": ["A", "A", "B"],
        "col2": ["X", "X", "Y"]
    })
    with pytest.raises(ValueError):
        task_func(data, "col1", "col2")

def test_task_func_valid_input():
    data = pd.DataFrame({
        "col1": ["A", "A", "B"],
        "col2": ["X", "X", "Y"]
    })
    result = task_func(data, "col1", "col2")
    assert isinstance(result, float)