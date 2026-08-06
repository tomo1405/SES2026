import pytest
from src_0423 import task_func
import pandas as pd

def test_task_func_basic():
    # Create a sample DataFrame
    data = {
        'a': [1, 2, 3, 4, 5],
        'b': [5, 4, 3, 2, 1],
        'c': [2, 3, 4, 5, 6],
        'target': [1, 0, 1, 0, 1]
    }
    df = pd.DataFrame(data)

    # Call the function
    X_train, X_test, y_train, y_test = task_func(df, 'target')

    # Check that the returned values are DataFrames
    assert isinstance(X_train, pd.DataFrame)
    assert isinstance(X_test, pd.DataFrame)
    assert isinstance(y_train, pd.Series)
    assert isinstance(y_test, pd.Series)

    # Check that the target column is removed from X_train and X_test
    assert 'target' not in X_train.columns
    assert 'target' not in X_test.columns

    # Check that the specified column 'c' is removed from the DataFrame
    assert 'c' not in X_train.columns
    assert 'c' not in X_test.columns

    # Check that the split is correct
    assert len(X_train) + len(X_test) == len(df)
    assert len(y_train) + len(y_test) == len(df)

def test_task_func_no_column_to_remove():
    # Create a sample DataFrame without the column to remove
    data = {
        'a': [1, 2, 3, 4, 5],
        'b': [5, 4, 3, 2, 1],
        'target': [1, 0, 1, 0, 1]
    }
    df = pd.DataFrame(data)

    # Call the function
    X_train, X_test, y_train, y_test = task_func(df, 'target', column_to_remove='d')

    # Check that the specified column 'd' is not in the DataFrame, so no change should be made
    assert 'd' not in X_train.columns
    assert 'd' not in X_test.columns

def test_task_func_empty_dataframe():
    # Create an empty DataFrame
    df = pd.DataFrame()

    # Call the function
    with pytest.raises(ValueError):
        task_func(df, 'target')