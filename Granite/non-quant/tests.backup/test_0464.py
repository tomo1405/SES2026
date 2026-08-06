import pytest
from src_0464 import task_func

def test_task_func():
    data_str = "1,2,3,4,5"
    separator = ","
    bins = 20
    expected_output = (pd.Series([1,2,3,4,5], dtype='int64'), ...)

    output = task_func(data_str, separator, bins)

    assert output == expected_output, "Output does not match expected output"