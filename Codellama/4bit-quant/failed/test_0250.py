import pytest
from src_0250 import task_func

def test_task_func():
    # Test that the function returns a tuple of two DataFrames
    train_data, test_data = task_func()
    assert isinstance(train_data, pd.DataFrame)
    assert isinstance(test_data, pd.DataFrame)

    # Test that the DataFrames have the correct number of rows
    assert len(train_data) == 8000
    assert len(test_data) == 2000

    # Test that the DataFrames have the correct number of columns
    assert len(train_data.columns) == 1
    assert len(test_data.columns) == 1

    # Test that the DataFrames have the correct column names
    assert train_data.columns[0] == 'Value'
    assert test_data.columns[0] == 'Value'

    # Test that the DataFrames have the correct data types
    assert train_data.dtypes[0] == float
    assert test_data.dtypes[0] == float

    # Test that the DataFrames have the correct data values
    assert train_data.iloc[0, 0] >= 0.0
    assert train_data.iloc[0, 0] <= 10.0
    assert test_data.iloc[0, 0] >= 0.0
    assert test_data.iloc[0, 0] <= 10.0

    # Test that the function raises a ValueError if the test_size is not between 0 and 1
    with pytest.raises(ValueError):
        task_func(test_size=-0.1)

    with pytest.raises(ValueError):
        task_func(test_size=1.1)