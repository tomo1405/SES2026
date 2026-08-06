import pytest
from src_0570 import task_func
import math
import inspect
import types

def test_task_func_no_defaults():
    def sample_function(a, b, c):
        pass

    expected_info = {
        'function_name': 'sample_function',
        'sqrt_args': math.sqrt(3),
        'lambda_in_defaults': 0
    }
    assert task_func(sample_function) == expected_info

def test_task_func_with_defaults():
    def sample_function(a, b, c, d=42, e=lambda x: x):
        pass

    expected_info = {
        'function_name': 'sample_function',
        'sqrt_args': math.sqrt(5),
        'lambda_in_defaults': 1
    }
    assert task_func(sample_function) == expected_info

def test_task_func_with_no_args():
    def sample_function():
        pass

    expected_info = {
        'function_name': 'sample_function',
        'sqrt_args': math.sqrt(0),
        'lambda_in_defaults': 0
    }
    assert task_func(sample_function) == expected_info

def test_task_func_with_lambdas_in_defaults():
    def sample_function(a, b, c, d=lambda x: x, e=lambda y: y + 1):
        pass

    expected_info = {
        'function_name': 'sample_function',
        'sqrt_args': math.sqrt(3),
        'lambda_in_defaults': 2
    }
    assert task_func(sample_function) == expected_info

def test_task_func_with_no_lambda_in_defaults():
    def sample_function(a, b, c, d=42, e=100):
        pass

    expected_info = {
        'function_name': 'sample_function',
        'sqrt_args': math.sqrt(5),
        'lambda_in_defaults': 0
    }
    assert task_func(sample_function) == expected_info