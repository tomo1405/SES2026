import pytest
from src_0567 import task_func

def test_task_func():
    # Test case 1: Basic function
    def example_function(a, b=1):
        pass

    result = task_func(example_function)
    assert result == {
        'function_name': 'example_function',
        'is_lambda': False,
        'args': ['a', 'b'],
        'defaults': (1,),
        'annotations': {}
    }

    # Add more test cases as needed

# Add more test cases as needed