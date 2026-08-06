import pytest
from src_0278 import task_func

def test_task_func_with_n_less_than_2():
    assert task_func(1) is None
    assert task_func(0) is None
    assert task_func(-5) is None

def test_task_func_with_n_equal_to_2():
    result = task_func(2)
    assert isinstance(result, tuple)
    assert len(result) == 2
    for point in result:
        assert isinstance(point, tuple)
        assert len(point) == 2
        for coord in point:
            assert isinstance(coord, float)

def test_task_func_with_n_greater_than_2():
    result = task_func(5)
    assert isinstance(result, tuple)
    assert len(result) == 2
    for point in result:
        assert isinstance(point, tuple)
        assert len(point) == 2
        for coord in point:
            assert isinstance(coord, float)

def test_task_func_consistency():
    random.seed(42)
    first_result = task_func(5)
    random.seed(42)
    second_result = task_func(5)
    assert first_result == second_result

def test_task_func_with_large_n():
    result = task_func(10)
    assert isinstance(result, tuple)
    assert len(result) == 2
    for point in result:
        assert isinstance(point, tuple)
        assert len(point) == 2
        for coord in point:
            assert isinstance(coord, float)