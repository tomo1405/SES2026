import pytest
from src_0552 import task_func

def test_task_func_empty_list():
    assert task_func([]) is None

def test_task_func_empty_sublist():
    assert task_func([[]]) is None

def test_task_func_single_item():
    assert task_func([['item1']]) is not None

def test_task_func_multiple_items():
    assert task_func([['item1', 'item2'], ['item3', 'item4']]) is not None

def test_task_func_duplicate_items():
    assert task_func([['item1', 'item2'], ['item2', 'item3']]) is not None

def test_task_func_invalid_input():
    with pytest.raises(TypeError):
        task_func(123)

def test_task_func_invalid_sublist():
    with pytest.raises(TypeError):
        task_func([123])