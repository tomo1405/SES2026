import pytest
from src_0561 import task_func

def test_task_func():
    data = "2022-01-10,2022-02-20,2022-03-30"
    ax = task_func(data)
    assert ax is not None

def test_task_func_empty_data():
    with pytest.raises(ValueError):
        task_func("")

def test_task_func_multiple_years():
    data = "2022-01-10,2023-02-20,2022-03-30"
    with pytest.raises(ValueError):
        task_func(data)