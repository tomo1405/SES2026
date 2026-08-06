import pandas as pd
import pytest
from src_0745 import task_func


def test_task_func_input_type():
    with pytest.raises(ValueError):
        task_func(123)

def test_task_func_output_type():
    assert isinstance(task_func("This is a test string"), pd.DataFrame)

def test_task_func_output_columns():
    df = task_func("This is a test string")
    assert df.columns.tolist() == ["Word", "Frequency"]

def test_task_func_output_values():
    df = task_func("This is a test string")
    assert df.loc[0, "Word"] == "This"
    assert df.loc[0, "Frequency"] == 1
    assert df.loc[1, "Word"] == "is"
    assert df.loc[1, "Frequency"] == 1
    assert df.loc[2, "Word"] == "a"
    assert df.loc[2, "Frequency"] == 1
    assert df.loc[3, "Word"] == "test"
    assert df.loc[3, "Frequency"] == 1
    assert df.loc[4, "Word"] == "string"
    assert df.loc[4, "Frequency"] == 1