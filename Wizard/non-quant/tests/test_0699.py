python
import pandas as pd
import pytest
from sklearn.model_selection import train_test_split

def task_func(df):
    X = pd.DataFrame.drop(df, 'target', axis=1)
    y = pd.DataFrame(df['target'])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    return X_train, X_test, y_train, y_test

def test_task_func():
    df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6], 'target': [7, 8, 9]})
    X_train, X_test, y_train, y_test = task_func(df)

    assert X_train.shape == (2, 2)
    assert X_test.shape == (1, 2)
    assert y_train.shape == (2, 1)
    assert y_test.shape == (1, 1)