import pytest
from src_0571 import task_func

def test_task_func():
    def example_function(a: int, b: str = 10):
        pass

    result = task_func(example_function)
    expected = {
        'function_name': 'example_function',
        'args': ['a', 'b'],
        'defaults': (10,),
        'annotations': {'a': 'int', 'b': 'int'},
        'is_lambda': False
    }
    assert result == json.dumps(expected)