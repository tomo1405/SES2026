import pytest
from src_0573 import task_func

def test_task_func():
    ax = task_func()
    assert ax is not None
    assert ax.get_ylabel() == 'Maximum Values'

def test_task_func_with_array_length():
    ax = task_func(array_length=10)
    assert ax is not None
    assert ax.get_ylabel() == 'Maximum Values'

def test_task_func_with_invalid_array_length():
    with pytest.raises(ValueError):
        task_func(array_length=-10)