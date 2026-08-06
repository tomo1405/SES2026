import pytest
from src_0828 import task_func
from sympy import isprime

def test_task_func_empty_list():
    assert task_func([]) == []

def test_task_func_no_primes():
    assert task_func([4, 6, 8, 9]) == []

def test_task_func_single_prime():
    assert task_func([3]) == [3]

def test_task_func_multiple_primes():
    assert task_func([2, 3, 5, 7, 11]) == [2, 3, 5, 7, 11]

def test_task_func_mixed_numbers():
    assert task_func([10, 11, 13, 17, 19, 23, 29, 31]) == [11, 13, 17, 19, 23, 29, 31]

def test_task_func_with_non_integers():
    with pytest.raises(TypeError):
        task_func([2, 3, 'a', 5])

def test_task_func_with_negative_numbers():
    assert task_func([-3, -2, -1, 0, 1, 2, 3]) == [2, 3]

def test_task_func_with_large_numbers():
    assert task_func([101, 103, 107, 109]) == [101, 103, 107, 109]