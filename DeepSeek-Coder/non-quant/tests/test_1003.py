import pytest
from src_1003 import task_func
import pandas as pd
import matplotlib.pyplot as plt

# Test cases for task_func
def test_task_func():
    # Test with a valid DataFrame
    data = {'target_column': [1, 2, 3, 4, 5]}
    df, _ = task_func(data)
    assert isinstance(df, pd.DataFrame), "The function should return a DataFrame"
    assert 'target_column' in df.columns, "The DataFrame should contain the target column"

    # Test with a non-numeric column
    data = {'non_numeric_column': ['a', 'b', 'c', 'd', 'e']}
    with pytest.raises(ValueError, match="Column 'non_numeric_column' not found in the DataFrame."):
        task_func(data)

    # Test with a numeric column
    data = {'numeric_column': [1, 2, 3, 4, 5]}
    df, _ = task_func(data, column_name='numeric_column')
    assert 'numeric_column' in df.columns, "The DataFrame should contain the target column"

    # Test with a non-existing column
    data = {'existing_column': [1, 2, 3, 4, 5]}
    with pytest.raises(ValueError, match="Column 'non_existing_column' not found in the DataFrame."):
        task_func(data, column_name='non_existing_column')

    # Test histogram plotting
    data = {'numeric_column': [1, 2, 3, 4, 5]}
    _, ax = task_func(data, column_name='numeric_column')
    assert ax is not None, "The histogram plot should be generated"