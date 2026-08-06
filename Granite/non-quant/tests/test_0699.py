import pandas as pd
from sklearn.model_selection import train_test_split
import pytest

def task_func(df):
    X = pd.DataFrame.drop(df, 'target', axis=1)
    y = pd.DataFrame(df['target'])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    return X_train, X_test, y_train, y_test

def test_task_func():
    # Create a sample dataframe for testing
    df = pd.DataFrame({
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [6, 7, 8, 9, 10],
        'target': [0, 1, 0, 1, 0]
    })

    # Call the function and store the returned values
    X_train, X_test, y_train, y_test = task_func(df)

    # Perform assertions to test the function's output
    assert len(X_train) == 3
    assert len(X_test) == 2
    assert len(y_train) == 3
    assert len(y_test) == 2
    assert X_train.columns.tolist() == ['feature1', 'feature2']
    assert X_test.columns.tolist() == ['feature1', 'feature2']
    assert y_train.columns.tolist() == ['target']
    assert y_test.columns.tolist() == ['target']

if __name__ == '__main__':
    pytest.main()