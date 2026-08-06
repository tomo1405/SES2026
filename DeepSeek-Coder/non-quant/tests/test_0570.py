import pytest
from src_0570 import task_func

def test_task_func():
    def example_function(a, b=1, *args, **kwargs):
        pass

    result = task_func(example_function)
    assert result == {
        'function_name': 'example_function',
        'sqrt_args': 1.0,
        'lambda_in_defaults': 0
    }