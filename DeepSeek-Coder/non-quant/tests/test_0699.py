import pytest
from src_0699 import task_func
import pandas as pd
from sklearn.model_selection import train_test_split

def test_task_func():
    # Create a sample DataFrame for testing
    data = {
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [5, 4, 3, 2, 1],
        'target': [0, 1, 0, 1, 0]
    }
    df = pd.DataFrame(data)

    # Call the function
    X_train, X_test, y_train, y_test = task_func(df)

    # Assertions to check the output
    assert isinstance(X_train, pd.DataFrame)
    assert isinstance(X_test, pd.DataFrame)
    assert isinstance(y_train, pd.DataFrame)
    assert isinstance(y_test, pd.DataFrame)

    # Add more assertions to check the content if necessary