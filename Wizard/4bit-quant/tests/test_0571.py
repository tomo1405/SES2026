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
    def test_func(a, b, c=1, d=2):
        pass

    assert task_func(test_func) == '{"function_name": "test_func", "args": ["a", "b"], "defaults": (1, 2), "annotations": {"a": "int", "b": "int", "c": "int", "d": "int"}, "is_lambda": false}'

    lambda_func = lambda x: x + 1
    assert task_func(lambda_func) == '{"function_name": "<lambda>", "args": ["x"], "defaults": null, "annotations": {"x": "int"}, "is_lambda": true}'

    def test_func_with_type_annotations(a: int, b: str, c: float = 1.0, d: bool = True) -> str:
        pass

    assert task_func(test_func_with_type_annotations) == '{"function_name": "test_func_with_type_annotations", "args": ["a", "b"], "defaults": (1.0, true), "annotations": {"a": "int", "b": "str", "c": "float", "d": "bool"}, "is_lambda": false}'