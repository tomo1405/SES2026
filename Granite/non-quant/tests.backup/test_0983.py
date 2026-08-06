import pytest
from src_0983 import task_func

def test_task_func():
    df = ...  # provide a sample DataFrame
    column = ...  # provide a sample column name
    ax = task_func(df, column)
    assert ax is not None  # check if the returned ax object is not None
    assert ax.get_title() == f"Normal Fit for '{column}'"  # check if the title is correct
    assert ax.get_ylabel() == "Density"  # check if the ylabel is correct
    assert ax.get_xlabel() == column  # check if the xlabel is correct