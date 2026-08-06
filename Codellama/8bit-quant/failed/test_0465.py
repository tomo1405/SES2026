import pytest
from src_0465 import task_func

def test_task_func():
    my_obj = {
        "name": "John Doe",
        "age": 30,
        "birthday": datetime(1990, 10, 10),
        "salary": Decimal("1000.00")
    }
    expected_result = '{"name": "John Doe", "age": 30, "birthday": "1990-10-10T00:00:00", "salary": "1000.00"}'
    assert task_func(my_obj) == expected_result