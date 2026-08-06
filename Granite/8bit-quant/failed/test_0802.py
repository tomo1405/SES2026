import pytest
from src_0802 import task_func
import numpy as np
import collections

def test_task_func_with_empty_file():
    file_name = "empty_file.csv"
    data = np.genfromtxt(file_name, delimiter=',', names=True, dtype=None, encoding=None)
    with pytest.raises(ValueError) as excinfo:
        task_func(file_name)
    assert "No data found in file" in str(excinfo.value)

def test_task_func_with_one_row_file():
    file_name = "one_row_file.csv"
    data = np.genfromtxt(file_name, delimiter=',', names=True, dtype=None, encoding=None)
    common_values = task_func(file_name)
    assert len(common_values) == len(data.dtype.names)
    for col in data.dtype.names:
        assert common_values[col] == data[col].item()

def test_task_func_with_multiple_rows_file():
    file_name = "multiple_rows_file.csv"
    data = np.genfromtxt(file_name, delimiter=',', names=True, dtype=None, encoding=None)
    common_values = task_func(file_name)
    assert len(common_values) == len(data.dtype.names)
    for col in data.dtype.names:
        counter = collections.Counter(data[col])
        if counter.most_common(2)[0][1] == counter.most_common(2)[1][1]:
            assert common_values[col] == sorted(counter.items())[0][0]
        else:
            assert common_values[col] == counter.most_common(1)[0][0]