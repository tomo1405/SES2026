import pytest
from src_0464 import task_func

def test_task_func_valid_data():
    data_str = "1,2,3,4,5"
    data, ax = task_func(data_str)
    assert data.size == 5
    assert ax.get_xlabel() == "data"
    assert ax.get_ylabel() == "count"

def test_task_func_invalid_data():
    data_str = ""
    with pytest.raises(ValueError):
        task_func(data_str)

def test_task_func_custom_separator():
    data_str = "1|2|3|4|5"
    data, ax = task_func(data_str, separator="|")
    assert data.size == 5
    assert ax.get_xlabel() == "data"
    assert ax.get_ylabel() == "count"

def test_task_func_custom_bins():
    data_str = "1,2,3,4,5"
    data, ax = task_func(data_str, bins=10)
    assert data.size == 5
    assert ax.get_xlabel() == "data"
    assert ax.get_ylabel() == "count"
    assert ax.get_xticks() == [1, 2, 3, 4, 5]
    assert ax.get_yticks() == [1, 2, 3, 4, 5]