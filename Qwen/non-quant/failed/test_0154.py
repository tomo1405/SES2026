import pytest
from src_0154 import task_func
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def test_task_func_with_unique_categories():
    # Test with unique categories
    data = ['apple', 'banana', 'cherry']
    expected_output = pd.DataFrame({
        'Category': ['apple', 'banana', 'cherry'],
        'Encoded': [0, 1, 2]
    })
    result = task_func(data)
    pd.testing.assert_frame_equal(result, expected_output)

def test_task_func_with_repeated_categories():
    # Test with repeated categories
    data = ['apple', 'banana', 'apple', 'cherry', 'banana']
    expected_output = pd.DataFrame({
        'Category': ['apple', 'banana', 'apple', 'cherry', 'banana'],
        'Encoded': [0, 1, 0, 2, 1]
    })
    result = task_func(data)
    pd.testing.assert_frame_equal(result, expected_output)

def test_task_func_with_single_category():
    # Test with a single category
    data = ['apple', 'apple', 'apple']
    expected_output = pd.DataFrame({
        'Category': ['apple', 'apple', 'apple'],
        'Encoded': [0, 0, 0]
    })
    result = task_func(data)
    pd.testing.assert_frame_equal(result, expected_output)

def test_task_func_with_empty_list():
    # Test with an empty list
    data = []
    expected_output = pd.DataFrame(columns=['Category', 'Encoded'])
    result = task_func(data)
    pd.testing.assert_frame_equal(result, expected_output)

def test_task_func_with_single_element():
    # Test with a single element
    data = ['apple']
    expected_output = pd.DataFrame({
        'Category': ['apple'],
        'Encoded': [0]
    })
    result = task_func(data)
    pd.testing.assert_frame_equal(result, expected_output)