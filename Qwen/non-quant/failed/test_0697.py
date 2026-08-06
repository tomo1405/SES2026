import pytest
from src_0697 import task_func

def test_task_func_zero_radius():
    result = task_func(0, 5)
    assert result == [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]

def test_task_func_single_point():
    result = task_func(1, 1)
    assert len(result) == 1
    x, y = result[0]
    assert -1 <= x <= 1
    assert -1 <= y <= 1

def test_task_func_multiple_points():
    result = task_func(1, 10)
    assert len(result) == 10
    for x, y in result:
        assert -1 <= x <= 1
        assert -1 <= y <= 1

def test_task_func_large_radius():
    result = task_func(10, 3)
    assert len(result) == 3
    for x, y in result:
        assert -10 <= x <= 10
        assert -10 <= y <= 10

def test_task_func_no_points():
    result = task_func(5, 0)
    assert result == []

def test_task_func_negative_radius():
    with pytest.raises(ValueError):
        task_func(-1, 5)

def test_task_func_non_integer_points():
    with pytest.raises(TypeError):
        task_func(1, 5.5)