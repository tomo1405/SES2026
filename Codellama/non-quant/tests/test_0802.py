import collections

import numpy as np
from src_0802 import task_func


def test_task_func_empty_file():
    file_name = "empty_file.csv"
    data = np.genfromtxt(file_name, delimiter=',', names=True,
                         dtype=None, encoding=None)
    common_values = task_func(file_name)
    assert common_values == {}


def test_task_func_single_row():
    file_name = "single_row.csv"
    data = np.genfromtxt(file_name, delimiter=',', names=True,
                         dtype=None, encoding=None)
    common_values = task_func(file_name)
    assert common_values == {col: data[col].item() for col in data.dtype.names}


def test_task_func_multiple_rows():
    file_name = "multiple_rows.csv"
    data = np.genfromtxt(file_name, delimiter=',', names=True,
                         dtype=None, encoding=None)
    common_values = task_func(file_name)
    for col in data.dtype.names:
        counter = collections.Counter(data[col])
        if counter.most_common(2)[0][1] == counter.most_common(2)[1][1]:
            assert common_values[col] == sorted(counter.items())[0][0]
        else:
            assert common_values[col] == counter.most_common(1)[0][0]