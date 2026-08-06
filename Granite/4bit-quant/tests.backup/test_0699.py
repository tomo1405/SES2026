import pandas as pd
from sklearn.model_selection import train_test_split

def task_func(df):
    X = pd.DataFrame.drop(df, 'target', axis=1)
    y = pd.DataFrame(df['target'])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    return X_train, X_test, y_train, y_test
import pytest

def test_task_func():
    # Create a sample dataframe for testing
    df = pd.DataFrame({
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [6, 7, 8, 9, 10],
        'target': [0, 1, 0, 1, 0]
    })

    # Call the function with the sample dataframe
    X_train, X_test, y_train, y_test = task_func(df)

    # Assert the output is correct
    assert X_train.shape == (3, 2)
    assert X_test.shape == (2, 2)
    assert y_train.shape == (3, 1)
    assert y_test.shape == (2, 1)

if __name__ == '__main__':
    pytest.main()