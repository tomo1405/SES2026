import pytest
from src_0423 import task_func

def test_task_func():
    # Test case 1: Test that the function returns the correct data types
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]})
    X_train, X_test, y_train, y_test = task_func(df, "a")
    assert isinstance(X_train, pd.DataFrame)
    assert isinstance(X_test, pd.DataFrame)
    assert isinstance(y_train, pd.Series)
    assert isinstance(y_test, pd.Series)

    # Test case 2: Test that the function drops the specified column if it exists in the dataframe
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]})
    X_train, X_test, y_train, y_test = task_func(df, "a", column_to_remove="b")
    assert "b" not in X_train.columns
    assert "b" not in X_test.columns

    # Test case 3: Test that the function splits the dataframe into training and test datasets
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]})
    X_train, X_test, y_train, y_test = task_func(df, "a", test_size=0.5)
    assert len(X_train) == 3
    assert len(X_test) == 3
    assert len(y_train) == 3
    assert len(y_test) == 3

    # Test case 4: Test that the function raises an error if the target column is not in the dataframe
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]})
    with pytest.raises(ValueError):
        task_func(df, "d")