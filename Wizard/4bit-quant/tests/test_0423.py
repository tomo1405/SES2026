python
import pandas as pd
import pytest
from sklearn.model_selection import train_test_split
from src_0423 import task_func

def test_task_func():
    # Test case 1: Test with valid input data
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
    target_column = 'a'
    column_to_remove = 'c'
    test_size = 0.2
    X_train, X_test, y_train, y_test = task_func(df, target_column, column_to_remove, test_size)
    assert X_train.shape == (2, 2)
    assert X_test.shape == (1, 2)
    assert y_train.shape == (2,)
    assert y_test.shape == (1,)

    # Test case 2: Test with invalid input data
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
    target_column = 'a'
    column_to_remove = 'd'
    test_size = 0.2
    with pytest.raises(ValueError):
        X_train, X_test, y_train, y_test = task_func(df, target_column, column_to_remove, test_size)