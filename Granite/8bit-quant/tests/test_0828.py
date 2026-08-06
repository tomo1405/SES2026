import pytest
from src_0828 import task_func
import math
from sympy import isprime

def test_task_func():
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    primes = [i for i in input_list if isprime(i)]
    sorted_primes = sorted(primes, key=lambda x: (math.degrees(x), x))
    assert task_func(input_list) == sorted_primes

def test_task_func_empty_list():
    input_list = []
    assert task_func(input_list) == []

def test_task_func_one_element_list():
    input_list = [2]
    assert task_func(input_list) == [2]

def test_task_func_negative_numbers():
    input_list = [-1, 2, -3, 4, -5]
    primes = [i for i in input_list if isprime(i)]
    sorted_primes = sorted(primes, key=lambda x: (math.degrees(x), x))
    assert task_func(input_list) == sorted_primes

def test_task_func_float_numbers():
    input_list = [1.1, 2.2, 3.3, 4.4, 5.5]
    primes = [i for i in input_list if isprime(i)]
    sorted_primes = sorted(primes, key=lambda x: (math.degrees(x), x))
    assert task_func(input_list) == sorted_primes