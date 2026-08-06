import itertools
import string

from src_1031 import task_func


def test_task_func():
    # Call the function
    df = task_func()

    # Check if the DataFrame has the correct columns
    assert list(df.columns) == ["Letter 1", "Letter 2", "Letter 3"]

    # Check if the DataFrame has the correct number of rows
    expected_rows = len(list(itertools.product(string.ascii_lowercase, repeat=3)))
    assert len(df) == expected_rows

    # Check if the DataFrame contains the correct data types
    assert all(isinstance(value, str) for value in df.values.flatten())

    # Check if the DataFrame contains the correct unique values
    unique_values = set(df.values.flatten())
    assert unique_values == set(string.ascii_lowercase)

    # Check if the DataFrame is sorted correctly
    assert df.is_sorted == True

    # Check if the DataFrame is not empty
    assert not df.empty