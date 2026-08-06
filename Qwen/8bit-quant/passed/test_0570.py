import pytest
from src_0570 import task_func
import inspect
import types
import math

def test_task_func_no_args():
    def sample_func():
        pass

    result = task_func(sample_func)
    assert result == {
        'function_name': 'sample_func',
        'sqrt_args': math.sqrt(0),
        'lambda_in_defaults': 0
    }

def test_task_func_with_args():
    def sample_func(a, b, c):
        pass

    result = task_func(sample_func)
    assert result == {
        'function_name': 'sample_func',
        'sqrt_args': math.sqrt(3),
        'lambda_in_defaults': 0
    }

def test_task_func_with_defaults():
    def sample_func(a, b, c=42):
        pass

    result = task_func(sample_func)
    assert result == {
        'function_name': 'sample_func',
        'sqrt_args': math.sqrt(3),
        'lambda_in_defaults': 0
    }

def test_task_func_with_lambda_in_defaults():
    def sample_func(a, b, c=lambda x: x):
        pass

    result = task_func(sample_func)
    assert result == {
        'function_name': 'sample_func',
        'sqrt_args': math.sqrt(3),
        'lambda_in_defaults': 1
    }

def test_task_func_with_multiple_lambdas_in_defaults():
    def sample_func(a, b, c=lambda x: x, d=lambda y: y):
        pass

    result = task_func(sample_func)
    assert result == {
        'function_name': 'sample_func',
        'sqrt_args': math.sqrt(4),
        'lambda_in_defaults': 2
    }

def test_task_func_with_no_defaults():
    def sample_func(a, b, c):
        pass

    result = task_func(sample_func)
    assert result == {
        'function_name': 'sample_func',
        'sqrt_args': math.sqrt(3),
        'lambda_in_defaults': 0
    }