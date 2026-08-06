import pandas as pd
import pytest
from src_0464 import task_func


def test_task_func():
    data_str = "1,2,3,4,5"
    separator = ","
    bins = 20
    expected_output = (pd.Series([1,2,3,4,5], dtype='int64'), ...)

    output = task_func(data_str, separator, bins)
    assert output == expected_output, "Output does not match expected output"

def test_task_func_with_invalid_data():
    data_str = "abc"
    separator = ","
    bins = 20

    with pytest.raises(ValueError) as excinfo:
        task_func(data_str, separator, bins)
    assert "Failed to find valid data" in str(excinfo.value), "Invalid data error message not raised"