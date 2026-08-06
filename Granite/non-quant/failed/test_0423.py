import pandas as pd
from sklearn.model_selection import train_test_split
import pytest

def task_func(df, target_column, column_to_remove="c", test_size=0.2):
    df = pd.DataFrame(df)
    if column_to_remove in df.columns:
        df = df.drop(columns=column_to_remove)
    X_train, X_test, y_train, y_test = train_test_split(
        df.drop(columns=target_column), df[target_column], test_size=test_size
    )
    return X_train, X_test, y_train, y_test

def test_task_func():
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9], 'target': [0, 1, 0]})
    X_train, X_test, y_train, y_test = task_func(df, 'target')
    assert isinstance(X_train, pd.DataFrame)
    assert isinstance(X_test, pd.DataFrame)
    assert isinstance(y_train, pd.Series)
    assert isinstance(y_test, pd.Series)
    assert X_train.shape[0] + X_test.shape[0] == df.shape[0]
    assert y_train.shape[0] + y_test.shape[0] == df.shape[0]
    assert set(X_train.columns) == {'a', 'b'}
    assert set(X_test.columns) == {'a', 'b'}
    assert set(y_train.name) == {'target'}
    assert set(y_test.name) == {'target'}