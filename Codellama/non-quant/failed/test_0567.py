import pytest
from src_0567 import task_func

def test_task_func():
    def test_func(x, y):
        return x + y

    result = task_func(test_func)

    assert result['function_name'] == 'test_func'
    assert result['is_lambda'] == False
    assert result['args'] == ['x', 'y']
    assert result['defaults'] == None
    assert result['annotations'] == {}

def test_task_func_lambda():
    test_func = lambda x, y: x + y

    result = task_func(test_func)

    assert result['function_name'] == 'test_func'
    assert result['is_lambda'] == True
    assert result['args'] == ['x', 'y']
    assert result['defaults'] == None
    assert result['annotations'] == {}

def test_task_func_defaults():
    def test_func(x, y=1):
        return x + y

    result = task_func(test_func)

    assert result['function_name'] == 'test_func'
    assert result['is_lambda'] == False
    assert result['args'] == ['x', 'y']
    assert result['defaults'] == [1]
    assert result['annotations'] == {}

def test_task_func_annotations():
    def test_func(x: int, y: int) -> int:
        return x + y

    result = task_func(test_func)

    assert result['function_name'] == 'test_func'
    assert result['is_lambda'] == False
    assert result['args'] == ['x', 'y']
    assert result['defaults'] == None
    assert result['annotations'] == {'x': int, 'y': int, 'return': int}