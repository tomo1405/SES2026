import pytest
from src_0140 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def test_task_func_with_valid_dataframe():
    # Create a sample DataFrame with numeric data
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1]
    }
    df = pd.DataFrame(data)

    # Call the function
    axes = task_func(df)

    # Check if the number of axes matches the number of numeric columns
    assert len(axes) == 2

    # Check if each axis has the correct title
    assert axes[0].get_title() == 'A'
    assert axes[1].get_title() == 'B'

def test_task_func_with_non_numeric_dataframe():
    # Create a sample DataFrame with no numeric data
    data = {
        'A': ['a', 'b', 'c', 'd', 'e'],
        'B': ['e', 'd', 'c', 'b', 'a']
    }
    df = pd.DataFrame(data)

    # Test that the function raises a ValueError when there are no numeric columns
    with pytest.raises(ValueError, match="DataFrame contains no numeric columns."):
        task_func(df)

def test_task_func_with_empty_dataframe():
    # Create an empty DataFrame
    df = pd.DataFrame()

    # Test that the function raises a ValueError when the DataFrame is empty
    with pytest.raises(ValueError, match="The input must be a non-empty pandas DataFrame."):
        task_func(df)

def test_task_func_with_non_dataframe_input():
    # Test that the function raises a ValueError when the input is not a DataFrame
    with pytest.raises(ValueError, match="The input must be a non-empty pandas DataFrame."):
        task_func([1, 2, 3, 4, 5])

def test_task_func_with_single_numeric_column():
    # Create a sample DataFrame with a single numeric column
    data = {
        'A': [1, 2, 3, 4, 5]
    }
    df = pd.DataFrame(data)

    # Call the function
    axes = task_func(df)

    # Check if the number of axes matches the number of numeric columns
    assert len(axes) == 1

    # Check if the axis has the correct title
    assert axes[0].get_title() == 'A'

def test_task_func_with_multiple_numeric_columns():
    # Create a sample DataFrame with multiple numeric columns
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1],
        'C': [2.5, 3.5, 4.5, 5.5, 6.5]
    }
    df = pd.DataFrame(data)

    # Call the function
    axes = task_func(df)

    # Check if the number of axes matches the number of numeric columns
    assert len(axes) == 3

    # Check if each axis has the correct title
    assert axes[0].get_title() == 'A'
    assert axes[1].get_title() == 'B'
    assert axes[2].get_title() == 'C'