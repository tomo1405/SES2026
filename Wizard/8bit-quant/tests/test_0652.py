python
import pandas as pd
import time
import pytest

def task_func(df, target_value):
    start_time = time.time()
    # Convert dataframe to string type for uniform comparison
    dataframe = pd.DataFrame(df)
    dataframe = dataframe.astype(str)
    
    counts = dataframe.apply(lambda x: (x == target_value).sum())

    # Check if DataFrame is empty
    if not dataframe.empty:
        ax = counts.plot(kind='bar')
    else:
        ax = None
    end_time = time.time()  # End timing
    cost = f"Operation completed in {end_time - start_time} seconds."
    return counts, ax

def test_task_func():
    # Test case 1: Valid input
    df = {'col1': [1, 2, 3], 'col2': ['a', 'b', 'c']}
    target_value = 'a'
    expected_counts = pd.Series([1], index=['col2'])
    expected_ax = None
    counts, ax = task_func(df, target_value)
    assert counts.equals(expected_counts)
    assert ax == expected_ax
    
    # Test case 2: Empty DataFrame
    df = {}
    target_value = 'a'
    expected_counts = pd.Series([], dtype=int)
    expected_ax = None
    counts, ax = task_func(df, target_value)
    assert counts.equals(expected_counts)
    assert ax == expected_ax
    
    # Test case 3: Non-existent target value
    df = {'col1': [1, 2, 3], 'col2': ['a', 'b', 'c']}
    target_value = 'd'
    expected_counts = pd.Series([0, 0, 0], index=['col1', 'col2', 'col3'])
    expected_ax = None
    counts, ax = task_func(df, target_value)
    assert counts.equals(expected_counts)
    assert ax == expected_ax
    
    # Test case 4: Non-string target value
    df = {'col1': [1, 2, 3], 'col2': ['a', 'b', 'c']}
    target_value = 1
    expected_counts = pd.Series([0, 0, 0], index=['col1', 'col2', 'col3'])
    expected_ax = None
    counts, ax = task_func(df, target_value)
    assert counts.equals(expected_counts)
    assert ax == expected_ax
    
    # Test case 5: Non-numeric target value
    df = {'col1': [1, 2, 3], 'col2': ['a', 'b', 'c']}
    target_value = '1'
    expected_counts = pd.Series([0, 0, 0], index=['col1', 'col2', 'col3'])
    expected_ax = None
    counts, ax = task_func(df, target_value)
    assert counts.equals(expected_counts)
    assert ax == expected_ax