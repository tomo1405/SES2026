import pytest
import inspect
import types
import json

def task_func(f):
    spec = inspect.getfullargspec(f)
    annotations = {k: v.__name__ if isinstance(v, type) else str(v) for k, v in spec.annotations.items()}

    info = {
        'function_name': f.__name__,
        'args': spec.args,
        'defaults': spec.defaults,
        'annotations': annotations,
        'is_lambda': isinstance(f, types.LambdaType)
    }

    return json.dumps(info)

def test_task_func():
    def sample_function(x, y):
        return x + y

    expected_output = '{"function_name": "sample_function", "args": ["x", "y"], "defaults": None, "annotations": {"x": "int", "y": "int"}, "is_lambda": false}'
    actual_output = task_func(sample_function)
    assert actual_output == expected_output

def test_task_func_with_lambda():
    lambda_func = lambda x, y: x + y

    expected_output = '{"function_name": "<lambda>", "args": ["x", "y"], "defaults": None, "annotations": {"x": "int", "y": "int"}, "is_lambda": true}'
    actual_output = task_func(lambda_func)
    assert actual_output == expected_output