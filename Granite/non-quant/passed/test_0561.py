import pytest
from src_0561 import task_func

def test_task_func():
    data = "2022-01-10,2022-02-20,2022-03-30"
    ax = task_func(data)
    assert ax is not None
    assert ax.get_xlabel() == 'Month'
    assert ax.get_ylabel() == 'Value'
    assert ax.get_title() == 'Monthly Data for 2022'

def test_task_func_empty_data():
    with pytest.raises(ValueError) as exc_info:
        task_func("")
    assert "The provided data string is empty." in str(exc_info.value)

def test_task_func_multiple_years():
    data = "2022-01-10,2023-02-20,2022-03-30"
    with pytest.raises(ValueError) as exc_info:
        task_func(data)
    assert "The provided data contains entries from multiple years." in str(exc_info.value)