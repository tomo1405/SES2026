import pandas as pd
import pytest
from src_0572 import task_func


def test_task_func():
    # Test that all elements in f_list must be callable functions
    with pytest.raises(ValueError):
        task_func([1, 2, 3], "test.csv")

    # Test that f_list should not be empty
    with pytest.raises(ValueError):
        task_func([], "test.csv")

    # Test that file_path must be a string
    with pytest.raises(ValueError):
        task_func([lambda x: x, lambda x: x], 123)

    # Test that the function returns a DataFrame with the correct columns
    df = task_func([lambda x: x, lambda x: x], "test.csv")
    assert isinstance(df, pd.DataFrame)
    assert df.columns.tolist() == ['Function Name', 'Number of Arguments', 'Defaults', 'Annotations', 'Is Lambda']

    # Test that the function raises an IOError if there is an error writing to the file
    with pytest.raises(IOError):
        task_func([lambda x: x, lambda x: x], "test.csv")