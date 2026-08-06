import pytest
from src_0423 import task_func
import pandas as pd
from sklearn.model_selection import train_test_split

def test_task_func():
    # Create a sample DataFrame
    data = {
        'a': [1, 2, 3, 4],
        'b': [5, 6, 7, 8],
        'c': [9, 10, 11, 12],
        'target': [13, 14, 15, 16]
    }
    df = pd.DataFrame(data)

    # Define expected output
    expected_columns = ['a', 'b', 'target']
    X_train_expected, X_test_expected, y_train_expected, y_test_expected = train_test_split(
        df[expected_columns[:-1]], df[expected_columns[-1]], test_size=0.2, random_state=42
    )

    # Call the function
    X_train, X_test, y_train, y_test = task_func(df, 'target', column_to_remove='c', test_size=0.2)

    # Check if the function returns the correct types
    assert isinstance(X_train, pd.DataFrame)
    assert isinstance(X_test, pd.DataFrame)
    assert isinstance(y_train, pd.Series)
    assert isinstance(y_test, pd.Series)

    # Check if the function returns the correct columns
    assert list(X_train.columns) == list(expected_columns[:-1])
    assert list(X_test.columns) == list(expected_columns[:-1])

    # Check if the function splits the data correctly
    assert len(X_train) + len(X_test) == len(df)
    assert len(y_train) + len(y_test) == len(df)

    # Check if the function handles the removal of the specified column
    assert 'c' not in X_train.columns
    assert 'c' not in X_test.columns

    # Check if the function handles the target column correctly
    assert 'target' not in X_train.columns
    assert 'target' not in X_test.columns

    # Check if the function returns the correct split sizes
    assert len(X_train) == len(X_train_expected)
    assert len(X_test) == len(X_test_expected)
    assert len(y_train) == len(y_train_expected)
    assert len(y_test) == len(y_test_expected)

    # Check if the function returns the correct values
    assert X_train.equals(X_train_expected)
    assert X_test.equals(X_test_expected)
    assert y_train.equals(y_train_expected)
    assert y_test.equals(y_test_expected)

# Run the tests
if __name__ == "__main__":
    pytest.main()