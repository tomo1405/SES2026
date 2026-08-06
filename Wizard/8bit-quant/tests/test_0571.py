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
    def my_func(a: int, b: str, c=True) -> float:
        pass

    assert task_func(my_func) == '{"function_name": "my_func", "args": ["a", "b", "c"], "defaults": (True,), "annotations": {"a": "int", "b": "str", "c": "bool"}, "is_lambda": false}'

    my_lambda = lambda x: x + 1
    assert task_func(my_lambda) == '{"function_name": "<lambda>", "args": ["x"], "defaults": null, "annotations": {}, "is_lambda": true}'