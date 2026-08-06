import pytest
from src_0654 import task_func

def test_task_func():
    # Mock the input dataframe
    dataframe = ...

    # Call the function
    mask, ax = task_func(dataframe)

    # Assert the expected output
    expected_mask = ...
    expected_ax = ...
    assert mask.equals(expected_mask)
    assert ax == expected_ax