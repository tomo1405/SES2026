import pytest
from src_0901 import task_func


def test_task_func_valid_input():
    d = [{'x': 1, 'y': 2, 'z': 3}, {'x': 4, 'y': 5, 'z': 6}]
    stats = task_func(d)
    assert isinstance(stats, dict)
    assert set(stats.keys()) == {'x', 'y', 'z'}
    for key, value in stats.items():
        if value is not None:
            assert isinstance(value, dict)
            assert set(value.keys()) == {'mean', 'sum', 'max', 'min', 'std'}

def test_task_func_invalid_input():
    d = 'not a list'
    with pytest.raises(ValueError) as exc_info:
        task_func(d)
    assert str(exc_info.value) == "Input must be a list of dictionaries."

def test_task_func_empty_input():
    d = []
    stats = task_func(d)
    assert isinstance(stats, dict)
    assert set(stats.keys()) == {'x', 'y', 'z'}
    for key, value in stats.items():
        assert value is None

def test_task_func_missing_values():
    d = [{'x': 1, 'y': 2}, {'x': 3, 'y': 4, 'z': 5}]
    stats = task_func(d)
    assert isinstance(stats, dict)
    assert set(stats.keys()) == {'x', 'y', 'z'}
    for key, value in stats.items():
        if value is not None:
            assert isinstance(value, dict)
            assert set(value.keys()) == {'mean', 'sum', 'max', 'min', 'std'}