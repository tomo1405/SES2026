import pytest
from src_0985 import task_func

def test_task_func():
    # Mock input data
    df = ...
    x_column = ...
    y_column = ...

    # Call the function
    ax = task_func(df, x_column, y_column)

    # Assert the output
    assert ax is not None
    assert ax.get_xlabel() == x_column
    assert ax.get_ylabel() == y_column