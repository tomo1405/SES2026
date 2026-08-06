import pytest
from src_1074 import task_func

def test_task_func():
    time_strings = ["12/01/2022 12:00:00.000", "12/01/2022 12:00:01.000", "12/01/2022 12:00:02.000"]
    ax = task_func(time_strings)
    assert ax is not None
    assert len(ax.patches) == 3
    assert ax.patches[0].get_height() == 1
    assert ax.patches[1].get_height() == 2
    assert ax.patches[2].get_height() == 3

def test_task_func_invalid_time_format():
    time_strings = ["12/01/2022 12:00:00.000", "12/01/2022 12:00:01.000", "12/01/2022 12:00:02.000"]
    ax = task_func(time_strings, time_format="%d/%m/%Y %H:%M:%S")
    assert ax is None

def test_task_func_invalid_time_strings():
    time_strings = ["12/01/2022 12:00:00.000", "12/01/2022 12:00:01.000", "12/01/2022 12:00:02.000"]
    ax = task_func(time_strings, time_format="%d/%m/%Y %H:%M:%S.%f")
    assert ax is None