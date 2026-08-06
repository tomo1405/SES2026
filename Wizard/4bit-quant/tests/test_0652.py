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
    df = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
    target_value = '5'
    expected_counts = pd.Series([0, 1, 0])
    expected_ax = None
    counts, ax = task_func(df, target_value)
    assert counts.equals(expected_counts)
    assert ax == expected_ax
    
    # Test case 2: Empty DataFrame
    df = {}
    target_value = '5'
    expected_counts = pd.Series([])
    expected_ax = None
    counts, ax = task_func(df, target_value)
    assert counts.equals(expected_counts)
    assert ax == expected_ax
    
    # Test case 3: Invalid input
    df = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
    target_value = '7'
    with pytest.raises(ValueError):
        task_func(df, target_value)