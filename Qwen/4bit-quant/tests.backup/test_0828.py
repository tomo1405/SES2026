import pytest
from src_0828 import task_func

def test_task_func_with_no_primes():
    assert task_func([4, 6, 8, 9]) == []

def test_task_func_with_one_prime():
    assert task_func([3, 4, 6, 8]) == [3]

def test_task_func_with_multiple_primes():
    assert task_func([2, 3, 5, 7, 11, 13]) == [2, 3, 5, 7, 11, 13]

def test_task_func_with_duplicates():
    assert task_func([2, 2, 3, 3, 5, 5]) == [2, 2, 3, 3, 5, 5]

def test_task_func_with_negative_and_zero():
    assert task_func([-1, 0, 1, 2, 3]) == [2, 3]

def test_task_func_with_large_numbers():
    assert task_func([101, 103, 107, 109, 113]) == [101, 103, 107, 109, 113]

def test_task_func_with_mixed_types():
    with pytest.raises(TypeError):
        task_func([2, 3, 'a', 5])