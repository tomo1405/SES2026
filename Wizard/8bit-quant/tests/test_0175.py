python
import pandas as pd
import numpy as np
import pytest

def task_func(data, key, min_value, max_value):
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input 'data' must be a pandas DataFrame.")
    
    random_generated = np.random.randint(min_value, max_value + 1, size=len(data))
    data[key] = random_generated
    return data

def test_task_func():
    # Test case 1: Valid input
    data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    key = 'C'
    min_value = 0
    max_value = 10
    expected_result = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    assert task_func(data, key, min_value, max_value).equals(expected_result)

    # Test case 2: Invalid input (not a DataFrame)
    data = [1, 2, 3]
    key = 'C'
    min_value = 0
    max_value = 10
    with pytest.raises(ValueError):
        task_func(data, key, min_value, max_value)

    # Test case 3: Invalid input (key already exists)
    data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    key = 'C'
    min_value = 0
    max_value = 10
    with pytest.raises(ValueError):
        task_func(data, key, min_value, max_value)