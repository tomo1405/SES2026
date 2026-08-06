import pytest
from src_0571 import task_func

def test_task_func():
    def test_func(x: int, y: str = 'hello'):
        pass

    info = task_func(test_func)
    assert info['function_name'] == 'test_func'
    assert info['args'] == ['x', 'y']
    assert info['defaults'] == ['hello']
    assert info['annotations'] == {'x': 'int', 'y': 'str'}
    assert info['is_lambda'] == False