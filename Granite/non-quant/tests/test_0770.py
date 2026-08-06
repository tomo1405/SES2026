import pytest
from src_0770 import task_func

def test_task_func():
    list_of_menuitems = [['a', 'b', 'c'], ['d', 'e', 'f'], ['a', 'b', 'e']]
    expected_output = 'a'
    actual_output = task_func(list_of_menuitems)
    assert actual_output == expected_output, "Expected output does not match actual output"

def test_task_func_with_empty_list():
    list_of_menuitems = [[]]
    expected_output = None
    actual_output = task_func(list_of_menuitems)
    assert actual_output == expected_output, "Expected output does not match actual output"

def test_task_func_with_single_item_list():
    list_of_menuitems = [['a']]
    expected_output = 'a'
    actual_output = task_func(list_of_menuitems)
    assert actual_output == expected_output, "Expected output does not match actual output"