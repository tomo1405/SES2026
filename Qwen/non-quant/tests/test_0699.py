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
    assert len(X_train) == 3
    assert len(X_test) == 2
    assert len(y_train) == 3
    assert len(y_test) == 2

    # Check that the splits are consistent with train_test_split
    X, y = df.drop('target', axis=1), df['target']
    X_train_expected, X_test_expected, y_train_expected, y_test_expected = train_test_split(X, y, test_size=0.3, random_state=42)
    
    assert X_train.equals(X_train_expected)
    assert X_test.equals(X_test_expected)
    assert y_train.equals(y_train_expected)
    assert y_test.equals(y_test_expected)