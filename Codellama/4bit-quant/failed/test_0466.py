import pytest
from src_0466 import task_func

def test_task_func():
    # Test with a datetime object
    my_obj = {"date": datetime.now()}
    result = task_func(my_obj)
    assert result == '{"date": "2023-02-28T12:00:00"}'

    # Test with a numpy array
    my_obj = {"array": np.array([1, 2, 3])}
    result = task_func(my_obj)
    assert result == '{"array": [1, 2, 3]}'

    # Test with a Decimal object
    my_obj = {"decimal": Decimal("1.23")}
    result = task_func(my_obj)
    assert result == '{"decimal": "1.23"}'

    # Test with a regular dict
    my_obj = {"key": "value"}
    result = task_func(my_obj)
    assert result == '{"key": "value"}'