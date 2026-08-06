import pytest
from src_0464 import task_func

def test_task_func():
    data_str = "1,2,3,4,5"
    separator = ","
    bins = 20
    data, ax = task_func(data_str, separator, bins)
    assert data.size == 5
    assert ax is not None

def test_task_func_with_invalid_data():
    data_str = "abc,def,ghi"
    separator = ","
    bins = 20
    with pytest.raises(ValueError):
        task_func(data_str, separator, bins)