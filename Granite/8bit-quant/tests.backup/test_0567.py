import pytest
from src_0567 import task_func

def test_task_func():
    def sample_function(a, b, c=10, d=20):
        return a + b + c + d

    result = task_func(sample_function)

    assert result['function_name'] == 'sample_function'
    assert result['is_lambda'] == False
    assert result['args'] == ['a', 'b', 'c', 'd']
    assert result['defaults'] == (10, 20)
    assert result['annotations'] == {}

def test_task_func_with_lambda():
    result = task_func(lambda x: x**2)

    assert result['function_name'] == '<lambda>'
    assert result['is_lambda'] == True
    assert result['args'] == ['x']
    assert result['defaults'] == None
    assert result['annotations'] == {}