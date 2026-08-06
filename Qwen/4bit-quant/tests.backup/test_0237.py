import pytest
from src_0237 import task_func
import pandas as pd

def test_task_func_with_valid_data():
    # Create a sample DataFrame
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, 35, 40, 45],
        'Score': [88, 92, 87, 94, 90],
        'Category': ['A', 'B', 'A', 'B', 'A']
    }
    df = pd.DataFrame(data)

    # Call the function
    accuracy = task_func(df)

    # Assert that the accuracy is a float between 0 and 1
    assert isinstance(accuracy, float)
    assert 0 <= accuracy <= 1

def test_task_func_with_invalid_input_type():
    # Test with a non-DataFrame input
    with pytest.raises(ValueError):
        task_func([1, 2, 3])

def test_task_func_with_no_duplicates():
    # Create a sample DataFrame with duplicates
    data = {
        'Name': ['Alice', 'Bob', 'Alice', 'David', 'Eve'],
        'Age': [25, 30, 25, 40, 45],
        'Score': [88, 92, 88, 94, 90],
        'Category': ['A', 'B', 'A', 'B', 'A']
    }
    df = pd.DataFrame(data)

    # Call the function
    accuracy = task_func(df)

    # Assert that the accuracy is a float between 0 and 1
    assert isinstance(accuracy, float)
    assert 0 <= accuracy <= 1

def test_task_func_with_custom_test_size_and_random_state():
    # Create a sample DataFrame
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, 35, 40, 45],
        'Score': [88, 92, 87, 94, 90],
        'Category': ['A', 'B', 'A', 'B', 'A']
    }
    df = pd.DataFrame(data)

    # Call the function with custom parameters
    accuracy = task_func(df, test_size=0.3, random_state=123)

    # Assert that the accuracy is a float between 0 and 1
    assert isinstance(accuracy, float)
    assert 0 <= accuracy <= 1