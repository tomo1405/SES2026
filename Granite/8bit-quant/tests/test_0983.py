import pytest
from src_0983 import task_func

def test_task_func():
    df = ...  # provide a sample input dataframe
    column = ...  # provide a sample column name
    ax = task_func(df, column)
    assert ax is not None  # check if the returned ax object is not None
    # add more assertions to check the output of the function