python
import inspect
import types
import json
import pytest

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
    def my_func(a, b, c=1, d=2):
        pass

    assert task_func(my_func) == '{"function_name": "my_func", "args": ["a", "b", "c", "d"], "defaults": (1, 2), "annotations": {"a": "Unknown", "b": "Unknown", "c": "int", "d": "int"}, "is_lambda": false}'

    my_lambda = lambda x, y: x + y
    assert task_func(my_lambda) == '{"function_name": "<lambda>", "args": ["x", "y"], "defaults": null, "annotations": {"x": "Unknown", "y": "Unknown"}, "is_lambda": true}'