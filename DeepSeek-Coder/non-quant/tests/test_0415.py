import pytest
from src_0415 import task_func
import pandas as pd
import numpy as np

@pytest.fixture
def sample_data():
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1],
        'C': [10, 20, 30, 40, 50]
    }
    return data

def test_task_func(sample_data):
    data = sample_data()
    result = task_func(data)
    assert result is not None

def test_task_func_with_no_numeric_data(sample_data):
    data = {
        'A': ['a', 'b', 'c', 'd', 'e'],
        'B': [1, 2, 3, 4, 5]
    }
    result = task_func(data)
    assert result[1] is None

def test_task_func_with_no_numeric_data(sample_data):
    data = {
        'A': ['a', 'b', 'c', 'd', 'e'],
        'B': [1, 2, 3, 4, 5]
    }
    result = task_func(data)
    assert result[1] is None