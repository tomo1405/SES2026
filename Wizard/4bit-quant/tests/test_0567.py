python
import inspect
import types
import pytest

def task_func(f):
    spec = inspect.getfullargspec(f)

    return {
        'function_name': f.__name__,
        'is_lambda': isinstance(f, types.LambdaType),
        'args': spec.args,
        'defaults': spec.defaults,
        'annotations': spec.annotations
    }

def test_task_func():
    # Test with a regular function
    def my_func(a, b, c=10):
        pass

    assert task_func(my_func) == {
        'function_name': 'my_func',
        'is_lambda': False,
        'args': ['a', 'b', 'c'],
        'defaults': (10,),
        'annotations': {}
    }

    # Test with a lambda function
    my_lambda = lambda x, y, z=20: x + y + z

    assert task_func(my_lambda) == {
        'function_name': '<lambda>',
        'is_lambda': True,
        'args': ['x', 'y', 'z'],
        'defaults': (20,),
        'annotations': {}
    }

    # Test with a generator function
    def my_gen(n):
        for i in range(n):
            yield i

    assert task_func(my_gen) == {
        'function_name': 'my_gen',
        'is_lambda': False,
        'args': ['n'],
        'defaults': None,
        'annotations': {}
    }

    # Test with a class method
    class MyClass:
        @staticmethod
        def my_method(a, b, c=30):
            pass

    assert task_func(MyClass.my_method) == {
        'function_name': 'my_method',
        'is_lambda': False,
        'args': ['a', 'b', 'c'],
        'defaults': (30,),
        'annotations': {}
    }

    # Test with a class method with annotations
    class MyClass:
        @staticmethod
        def my_method(a: int, b: str, c: float = 40.0) -> bool:
            pass

    assert task_func(MyClass.my_method) == {
        'function_name': 'my_method',
        'is_lambda': False,
        'args': ['a', 'b', 'c'],
        'defaults': (40.0,),
        'annotations': {'a': int, 'b': str, 'c': float, 'return': bool}
    }