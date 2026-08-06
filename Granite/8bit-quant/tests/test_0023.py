import pytest
from src_0023 import task_func

def test_task_func():
    l1 = [1, 2, 3]
    l2 = [4, 5, 6]
    K = 5
    expected_result = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}
    result = task_func(l1, l2, K)
    assert result == expected_result

def test_task_func_with_empty_lists():
    l1 = []
    l2 = []
    K = 10
    expected_result = {}
    result = task_func(l1, l2, K)
    assert result == expected_result

def test_task_func_with_uneven_lists():
    l1 = [1, 2, 3]
    l2 = [4, 5]
    K = 5
    expected_result = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}
    result = task_func(l1, l2, K)
    assert result == expected_result

def test_task_func_with_negative_k():
    l1 = [1, 2, 3]
    l2 = [4, 5, 6]
    K = -10
    with pytest.raises(ValueError) as excinfo:
        task_func(l1, l2, K)
    assert "k must be a non-negative integer" in str(excinfo.value)