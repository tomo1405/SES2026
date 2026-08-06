import pytest
from src_0175 import task_func
import pandas as pd
import numpy as np

def test_task_func():
    data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    key = 'C'
    min_value = 10
    max_value = 20
    expected_result = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [10, 11, 12]})
    result = task_func(data, key, min_value, max_value)
    assert result.equals(expected_result)

def test_task_func_invalid_input():
    data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    key = 'C'
    min_value = 10
    max_value = 20
    with pytest.raises(ValueError):
        task_func(data, key, min_value, max_value)