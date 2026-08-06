import pytest
from src_0567 import task_func

def test_task_func_with_lambda():
    f = lambda x: x + 1
    result = task_func(f)
    assert result['function_name'] == 'lambda'
    assert result['is_lambda'] == True
    assert result['args'] == ['x']
    assert result['defaults'] == None
    assert result['annotations'] == {}

def test_task_func_with_function():
    def f(x):
        return x + 1
    result = task_func(f)
    assert result['function_name'] == 'f'
    assert result['is_lambda'] == False
    assert result['args'] == ['x']
    assert result['defaults'] == None
    assert result['annotations'] == {}

def test_task_func_with_default_args():
    def f(x, y=1):
        return x + y
    result = task_func(f)
    assert result['function_name'] == 'f'
    assert result['is_lambda'] == False
    assert result['args'] == ['x', 'y']
    assert result['defaults'] == [1]
    assert result['annotations'] == {}

def test_task_func_with_annotations():
    def f(x: int, y: str) -> int:
        return x + 1
    result = task_func(f)
    assert result['function_name'] == 'f'
    assert result['is_lambda'] == False
    assert result['args'] == ['x', 'y']
    assert result['defaults'] == None
    assert result['annotations'] == {'x': int, 'y': str, 'return': int}