import pytest
from src_1084 import task_func
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

def test_task_func_valid_input():
    data = {
        "Salary_String": ["100000", "200000", "150000"],
        "Experience": [3, 5, 7]
    }
    result = task_func(data)
    assert result is not None, "The function should return a plot"

def test_task_func_invalid_input():
    data = {
        "Salary_String": ["100000", "200000", "150000"],
        "Experience": [3, 5, 7]
    }
    with pytest.raises(ValueError):
        task_func(data)

def test_task_func_empty_data():
    data = {}
    result = task_func(data)
    assert result is not None, "The function should return a plot for empty data"

def test_task_func_invalid_salary():
    data = {
        "Salary_String": ["100k", "200k", "150k"],
        "Experience": [3, 5, 7]
    }
    with pytest.raises(ValueError):
        task_func(data)