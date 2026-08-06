import pytest
from src_0423 import task_func
import pandas as pd
from sklearn.model_selection import train_test_split

def test_task_func():
    # Create a sample DataFrame
    data = {
        'a': [1, 2, 3, 4],
        'b': [5, 6, 7, 8],
        'c': [9, 10, 11, 12],
        'target': [13, 14, 15, 16]
    }
    df = pd.DataFrame(data)

    # Expected output after removing column 'c' and splitting
    expected_columns = ['a', 'b']
    expected_target = 'target'
    test_size = 0.2

    # Call the function
    X_train, X_test, y_train, y_test = task_func(df, target_column='target')

    # Check if the correct columns are present in the split datasets
    assert list(X_train.columns) == expected_columns
    assert list(X_test.columns) == expected_columns
    assert y_train.name == expected_target
    assert y_test.name == expected_target

    # Check if the split is correct
    assert len(X_train) + len(X_test) == len(df)
    assert len(X_test) == int(len(df) * test_size)

def test_task_func_column_removal():
    # Create a sample DataFrame with column 'c' to be removed
    data = {
        'a': [1, 2, 3, 4],
        'b': [5, 6, 7, 8],
        'c': [9, 10, 11, 12],
        'target': [13, 14, 15, 16]
    }
    df = pd.DataFrame(data)

    # Call the function with column_to_remove='c'
    X_train, X_test, y_train, y_test = task_func(df, target_column='target', column_to_remove='c')

    # Check if column 'c' is removed
    assert 'c' not in X_train.columns
    assert 'c' not in X_test.columns

def test_task_func_no_column_removal():
    # Create a sample DataFrame without column 'c'
    data = {
        'a': [1, 2, 3, 4],
        'b': [5, 6, 7, 8],
        'target': [13, 14, 15, 16]
    }
    df = pd.DataFrame(data)

    # Call the function with column_to_remove='d' (which doesn't exist)
    X_train, X_test, y_train, y_test = task_func(df, target_column='target', column_to_remove='d')

    # Check if no columns are removed
    assert list(X_train.columns) == ['a', 'b']
    assert list(X_test.columns) == ['a', 'b']

def test_task_func_invalid_target_column():
    # Create a sample DataFrame
    data = {
        'a': [1, 2, 3, 4],
        'b': [5, 6, 7, 8],
        'c': [9, 10, 11, 12],
        'target': [13, 14, 15, 16]
    }
    df = pd.DataFrame(data)

    # Call the function with an invalid target_column
    with pytest.raises(KeyError):
        task_func(df, target_column='invalid_column')