import pytest
from src_0521 import task_func

def test_task_func():
    data = [{"apple": 10, "banana": 20, "orange": 30}, {"apple": 5, "banana": 10, "orange": 15}]
    total_sales, ax = task_func(data)
    assert total_sales == {"apple": 15, "banana": 30, "orange": 45}
    assert ax.get_xlabel() == "Fruit"
    assert ax.get_ylabel() == "Total Sales"
    assert ax.get_title() == "Total Fruit Sales"

def test_task_func_empty_data():
    data = []
    total_sales, ax = task_func(data)
    assert total_sales == {}
    assert ax is None

def test_task_func_negative_sales():
    data = [{"apple": 10, "banana": 20, "orange": 30}, {"apple": 5, "banana": 10, "orange": -15}]
    with pytest.raises(ValueError):
        task_func(data)