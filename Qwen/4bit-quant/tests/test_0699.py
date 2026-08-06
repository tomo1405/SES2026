import pytest
from src_0699 import task_func
import pandas as pd
from sklearn.model_selection import train_test_split

def test_task_func():
    # Create a sample DataFrame
    data = {
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [5, 4, 3, 2, 1],
        'target': [0, 1, 0, 1, 0]
    }
    df = pd.DataFrame(data)

    # Call the function
    X_train, X_test, y_train, y_test = task_func(df)

    # Check that the splits are correct
    assert isinstance(X_train, pd.DataFrame)
    assert isinstance(X_test, pd.DataFrame)
    assert isinstance(y_train, pd.DataFrame)
    assert isinstance(y_test, pd.DataFrame)

    # Check that the sizes are correct
    assert len(X_train) == 3
    assert len(X_test) == 2
    assert len(y_train) == 3
    assert len(y_test) == 2

    # Check that the data is split correctly
    assert all(feature in X_train.columns for feature in ['feature1', 'feature2'])
    assert all(feature in X_test.columns for feature in ['feature1', 'feature2'])
    assert 'target' in y_train.columns
    assert 'target' in y_test.columns

    # Check that the random_state ensures reproducibility
    X_train2, X_test2, y_train2, y_test2 = task_func(df)
    assert X_train.equals(X_train2)
    assert X_test.equals(X_test2)
    assert y_train.equals(y_train2)
    assert y_test.equals(y_test2)