import pytest
from src_0552 import task_func

def test_task_func_empty_list():
    list_of_menuitems = []
    result = task_func(list_of_menuitems)
    assert result is None

def test_task_func_empty_sublist():
    list_of_menuitems = [[]]
    result = task_func(list_of_menuitems)
    assert result is None

def test_task_func_single_item():
    list_of_menuitems = [['item1']]
    result = task_func(list_of_menuitems)
    assert result is not None

def test_task_func_multiple_items():
    list_of_menuitems = [['item1', 'item2'], ['item3', 'item4']]
    result = task_func(list_of_menuitems)
    assert result is not None

def test_task_func_invalid_input():
    list_of_menuitems = [['item1', 'item2'], ['item3', 'item4'], 'item5']
    result = task_func(list_of_menuitems)
    assert result is None