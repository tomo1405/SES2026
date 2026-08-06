import pytest
from src_0561 import task_func

def test_task_func_with_empty_data():
    with pytest.raises(ValueError) as exc_info:
        task_func("")
    assert "The provided data string is empty." in str(exc_info.value)

def test_task_func_with_multiple_years():
    data = "2022-01,2023-01,2023-02"
    with pytest.raises(ValueError) as exc_info:
        task_func(data)
    assert "The provided data contains entries from multiple years." in str(exc_info.value)

def test_task_func_with_valid_data():
    data = "2022-01,2022-02,2022-03"
    ax = task_func(data)
    assert ax is not None