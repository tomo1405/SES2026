import pytest
from src_0154 import task_func
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def test_task_func():
    # Test with a simple list of categories
    data = ['apple', 'banana', 'orange', 'apple']
    expected_output = pd.DataFrame({
        'Category': ['apple', 'banana', 'orange', 'apple'],
        'Encoded': [0, 1, 2, 0]
    })
    output_df = task_func(data)
    assert output_df.equals(expected_output), "Test failed for simple list of categories"

    # Test with an empty list
    data = []
    expected_output = pd.DataFrame({
        'Category': [],
        'Encoded': []
    })
    output_df = task_func(data)
    assert output_df.equals(expected_output), "Test failed for empty list"

    # Test with a list containing one category
    data = ['apple']
    expected_output = pd.DataFrame({
        'Category': ['apple'],
        'Encoded': [0]
    })
    output_df = task_func(data)
    assert output_df.equals(expected_output), "Test failed for list with one category"

    # Test with a list containing repeated categories
    data = ['apple', 'apple', 'apple']
    expected_output = pd.DataFrame({
        'Category': ['apple', 'apple', 'apple'],
        'Encoded': [0, 0, 0]
    })
    output_df = task_func(data)
    assert output_df.equals(expected_output), "Test failed for list with repeated categories"