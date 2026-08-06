import pytest
from src_0395 import task_func

def test_task_func():
    # Test case 1: length = 10, seed = 0
    result = task_func(10, 0)
    assert len(result) == 10
    assert all(isinstance(key, str) and len(key) == 1 for key in result.keys())
    assert all(isinstance(value, int) for value in result.values())

    # Test case 2: length = 10, seed = 1
    result = task_func(10, 1)
    assert len(result) == 10
    assert all(isinstance(key, str) and len(key) == 1 for key in result.keys())
    assert all(isinstance(value, int) for value in result.values())

    # Test case 3: length = 10, seed = 2
    result = task_func(10, 2)
    assert len(result) == 10
    assert all(isinstance(key, str) and len(key) == 1 for key in result.keys())
    assert all(isinstance(value, int) for value in result.values())

    # Test case 4: length = 10, seed = 3
    result = task_func(10, 3)
    assert len(result) == 10
    assert all(isinstance(key, str) and len(key) == 1 for key in result.keys())
    assert all(isinstance(value, int) for value in result.values())

    # Test case 5: length = 10, seed = 4
    result = task_func(10, 4)
    assert len(result) == 10
    assert all(isinstance(key, str) and len(key) == 1 for key in result.keys())
    assert all(isinstance(value, int) for value in result.values())

    # Test case 6: length = 10, seed = 5
    result = task_func(10, 5)
    assert len(result) == 10
    assert all(isinstance(key, str) and len(key) == 1 for key in result.keys())
    assert all(isinstance(value, int) for value in result.values())

    # Test case 7: length = 10, seed = 6
    result = task_func(10, 6)
    assert len(result) == 10
    assert all(isinstance(key, str) and len(key) == 1 for key in result.keys())
    assert all(isinstance(value, int) for value in result.values())

    # Test case 8: length = 10, seed = 7
    result = task_func(10, 7)
    assert len(result) == 10
    assert all(isinstance(key, str) and len(key) == 1 for key in result.keys())
    assert all(isinstance(value, int) for value in result.values())

    # Test case 9: length = 10, seed = 8
    result = task_func(10, 8)
    assert len(result) == 10
    assert all(isinstance(key, str) and len(key) == 1 for key in result.keys())
    assert all(isinstance(value, int) for value in result.values())

    # Test case 10: length = 10, seed = 9
    result = task_func(10, 9)
    assert len(result) == 10
    assert all(isinstance(key, str) and len(key) == 1 for key in result.keys())
    assert all(isinstance(value, int) for value in result.values())