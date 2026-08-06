import pytest
from src_0571 import task_func

def test_task_func_no_args():
    def func():
        pass
    expected = '{"function_name": "func", "args": [], "defaults": null, "annotations": {}, "is_lambda": false}'
    assert task_func(func) == expected

def test_task_func_with_args():
    def func(a, b):
        pass
    expected = '{"function_name": "func", "args": ["a", "b"], "defaults": null, "annotations": {}, "is_lambda": false}'
    assert task_func(func) == expected

def test_task_func_with_defaults():
    def func(a, b=2):
        pass
    expected = '{"function_name": "func", "args": ["a", "b"], "defaults": [2], "annotations": {}, "is_lambda": false}'
    assert task_func(func) == expected

def test_task_func_with_annotations():
    def func(a: int, b: str) -> bool:
        pass
    expected = '{"function_name": "func", "args": ["a", "b"], "defaults": null, "annotations": {"a": "int", "b": "str", "return": "bool"}, "is_lambda": false}'
    assert task_func(func) == expected

def test_task_func_lambda():
    func = lambda x: x
    expected = '{"function_name": "<lambda>", "args": ["x"], "defaults": null, "annotations": {}, "is_lambda": true}'
    assert task_func(func) == expected

def test_task_func_complex_defaults():
    def func(a, b=(1, 2), c={'key': 'value'}):
        pass
    expected = '{"function_name": "func", "args": ["a", "b", "c"], "defaults": [(1, 2), {"key": "value"}], "annotations": {}, "is_lambda": false}'
    assert task_func(func) == expected