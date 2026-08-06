import pytest
import inspect
import types
import json
from src_0571 import task_func

def test_task_func():
    def simple_function(a, b):
        return a + b

    def lambda_function(a, b):
        return a * b

    assert task_func(simple_function) == '{"function_name": "simple_function", "args": ["a", "b"], "defaults": null, "annotations": {"a": "<class 'int'>", "b": "<class 'int'>"}, "is_lambda": false}'
    assert task_func(lambda_function) == '{"function_name": "lambda_function", "args": ["a", "b"], "defaults": null, "annotations": {"a": "<class 'int'>", "b": "<class 'int'>"}, "is_lambda": true}'