python
import pandas as pd
import pytest
from sklearn.model_selection import train_test_split
from src_0699 import task_func

def test_task_func():
    df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6], 'target': [7, 8, 9]})
    X_train, X_test, y_train, y_test = task_func(df)

    assert isinstance(X_train, pd.DataFrame)
    assert isinstance(X_test, pd.DataFrame)
    assert isinstance(y_train, pd.DataFrame)
    assert isinstance(y_test, pd.DataFrame)

    assert X_train.shape[0] == 2
    assert X_test.shape[0] == 1
    assert y_train.shape[0] == 2
    assert y_test.shape[0] == 1

    assert X_train.shape[1] == 1
    assert X_test.shape[1] == 1
    assert y_train.shape[1] == 1
    assert y_test.shape[1] == 1

    assert X_train.columns[0] == 'col1'
    assert X_test.columns[0] == 'col1'
    assert y_train.columns[0] == 'target'
    assert y_test.columns[0] == 'target'

    assert X_train.values[0][0] == 1
    assert X_test.values[0][0] == 3
    assert y_train.values[0][0] == 7
    assert y_test.values[0][0] == 9