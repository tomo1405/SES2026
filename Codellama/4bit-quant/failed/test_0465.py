import pytest
from src_0465 import task_func

def test_task_func():
    my_obj = {
        "name": "John Doe",
        "age": 30,
        "birthday": datetime.date(1990, 10, 10),
        "salary": Decimal("1234.56")
    }
    expected_result = '{"name": "John Doe", "age": 30, "birthday": "1990-10-10", "salary": "1234.56"}'
    assert task_func(my_obj) == expected_result

def test_task_func_with_invalid_input():
    my_obj = "invalid input"
    with pytest.raises(TypeError):
        task_func(my_obj)