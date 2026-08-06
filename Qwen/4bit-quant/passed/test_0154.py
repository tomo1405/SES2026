import pytest
from src_0154 import task_func
import pandas as pd

def test_task_func():
    # Test with a simple list of categories
    data = ['apple', 'banana', 'apple', 'orange']
    expected_output = pd.DataFrame({
        'Category': ['apple', 'banana', 'apple', 'orange'],
        'Encoded': [0, 1, 0, 2]
    })
    result = task_func(data)
    assert result.equals(expected_output)

    # Test with an empty list
    data = []
    expected_output = pd.DataFrame(columns=['Category', 'Encoded'])
    result = task_func(data)
    assert result.equals(expected_output)

    # Test with a single category
    data = ['apple']
    expected_output = pd.DataFrame({
        'Category': ['apple'],
        'Encoded': [0]
    })
    result = task_func(data)
    assert result.equals(expected_output)

    # Test with duplicate categories
    data = ['apple', 'apple', 'apple']
    expected_output = pd.DataFrame({
        'Category': ['apple', 'apple', 'apple'],
        'Encoded': [0, 0, 0]
    })
    result = task_func(data)
    assert result.equals(expected_output)

    # Test with mixed case categories
    data = ['Apple', 'apple', 'APPLE']
    expected_output = pd.DataFrame({
        'Category': ['Apple', 'apple', 'APPLE'],
        'Encoded': [0, 1, 2]
    })
    result = task_func(data)
    assert result.equals(expected_output)