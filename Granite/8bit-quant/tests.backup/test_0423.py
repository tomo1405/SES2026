import pandas as pd
import pytest
from sklearn.model_selection import train_test_split
from src_0423 import task_func

@pytest.fixture
def input_df():
    return pd.DataFrame({
        'a': [1, 2, 3, 4, 5],
        'b': [6, 7, 8, 9, 10],
        'c': [11, 12, 13, 14, 15],
        'd': [16, 17, 18, 19, 20]
    })

def test_task_func(input_df):
    X_train, X_test, y_train, y_test = task_func(input_df, 'd', 'c', 0.2)
    assert isinstance(X_train, pd.DataFrame)
    assert isinstance(X_test, pd.DataFrame)
    assert isinstance(y_train, pd.DataFrame)
    assert isinstance(y_test, pd.DataFrame)
    assert X_train.shape[1] + X_test.shape[1] == input_df.shape[1] - 1
    assert y_train.shape[1] + y_test.shape[1] == 1

def test_task_func_column_not_exists(input_df):
    X_train, X_test, y_train, y_test = task_func(input_df, 'd', 'e', 0.2)
    assert isinstance(X_train, pd.DataFrame)
    assert isinstance(X_test, pd.DataFrame)
    assert isinstance(y_train, pd.DataFrame)
    assert isinstance(y_test, pd.DataFrame)
    assert X_train.shape[1] + X_test.shape[1] == input_df.shape[1]
    assert y_train.shape[1] + y_test.shape[1] == 1

def test_task_func_invalid_target_column(input_df):
    with pytest.raises(ValueError):
        task_func(input_df, 'e', 'c', 0.2)

def test_task_func_invalid_test_size(input_df):
    with pytest.raises(ValueError):
        task_func(input_df, 'd', 'c', 1.2)