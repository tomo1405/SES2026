import pytest
from src_0828 import task_func
from sympy import isprime

def test_task_func_empty_list():
    assert task_func([]) == []

def test_task_func_no_primes():
    assert task_func([4, 6, 8, 9]) == []

def test_task_func_single_prime():
    assert task_func([2]) == [2]

def test_task_func_multiple_primes():
    assert task_func([3, 5, 7, 11]) == [3, 5, 7, 11]

def test_task_func_mixed_numbers():
    assert task_func([2, 4, 6, 7, 10, 11]) == [2, 7, 11]

def test_task_func_large_numbers():
    assert task_func([17, 19, 23, 29]) == [17, 19, 23, 29]

def test_task_func_negative_numbers():
    assert task_func([-3, -5, 2, 3]) == [2, 3]

def test_task_func_non_integer():
    with pytest.raises(TypeError):
        task_func([2, 3, 'a', 5])