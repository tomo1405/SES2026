import pytest
from src_0231 import task_func
import pandas as pd

def test_task_func():
    # Test case 1: Invalid input (not a DataFrame)
    invalid_input = "Invalid input"
    assert task_func("invalid input") == invalid_input

    # Test case 2: Valid input (DataFrame with duplicates)
    df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Alice', 'Charlie'],
        'Age': [25, 30, 25, 35],
        'Country': ['USA', 'Canada', 'USA', 'Australia'],
        'Score': [80, 90, 80, 75]
    })
    expected_output = "Invalid input"
    assert task_func(df) == expected_output

    # Test case 3: Valid input (DataFrame without duplicates)
    df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'Country': ['USA', 'Canada', 'Australia', 'Japan'],
        'Score': [80, 90, 75, 65]
    })
    expected_output = type(plt.figure())
    assert isinstance(task_func(df), expected_output)