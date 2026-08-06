import pytest
from src_0567 import task_func

def test_task_func():
    def sample_function(arg1, arg2, arg3=10, arg4=20):
        pass

    result = task_func(sample_function)
    assert result['function_name'] == 'sample_function'
    assert result['is_lambda'] == False
    assert result['args'] == ['arg1', 'arg2', 'arg3', 'arg4']
    assert result['defaults'] == (10, 20)
    assert result['annotations'] == {}

def test_task_func_with_lambda():
    result = task_func(lambda x: x + 1)
    assert result['function_name'] == '<lambda>'
    assert result['is_lambda'] == True
    assert result['args'] == ['x']
    assert result['defaults'] == None
    assert result['annotations'] == {}

def test_task_func_with_annotations():
    def sample_function(arg1: int, arg2: str, arg3: float = 10.0, arg4: bool = True) -> float:
        pass

    result = task_func(sample_function)
    assert result['function_name'] == 'sample_function'
    assert result['is_lambda'] == False
    assert result['args'] == ['arg1', 'arg2', 'arg3', 'arg4']
    assert result['defaults'] == (10.0, True)
    assert result['annotations'] == {'arg1': int, 'arg2': str, 'arg3': float, 'return': float}