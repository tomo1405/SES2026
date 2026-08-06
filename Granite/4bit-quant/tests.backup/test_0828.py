import math
from sympy import isprime
import pytest

def task_func(input_list):
    primes = [i for i in input_list if isprime(i)]
    sorted_primes = sorted(primes, key=lambda x: (math.degrees(x), x))
    return sorted_primes

def test_task_func():
    input_list = [2, 3, 5, 7, 11, 13, 17, 19]
    expected_output = [2, 3, 5, 7, 11, 13, 17, 19]
    actual_output = task_func(input_list)
    assert actual_output == expected_output, "Output does not match expected output"

test_task_func()