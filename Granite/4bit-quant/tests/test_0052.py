import pytest
from src_0052 import task_func

def test_task_func():
    # Mock the input data
    df = ...

    # Mock the expected output
    expected_selected_df = ...
    expected_ax = ...

    # Call the function and compare the output with the expected output
    selected_df, ax = task_func(df, age=25, height=65)
    assert selected_df.equals(expected_selected_df)
    assert ax == expected_ax

def test_task_func_with_invalid_input():
    # Mock an invalid input
    invalid_df = ...

    # Call the function with an invalid input and assert that it raises an exception
    with pytest.raises(Exception) as exc_info:
        task_func(invalid_df, age=25, height=65)
    assert "Invalid input" in str(exc_info.value)