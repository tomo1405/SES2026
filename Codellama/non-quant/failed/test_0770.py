import pytest
from src_0770 import task_func

def test_task_func():
    list_of_menuitems = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        ['g', 'h', 'i']
    ]
    expected_result = 'e'
    assert task_func(list_of_menuitems) == expected_result

def test_task_func_empty_list():
    list_of_menuitems = []
    expected_result = None
    assert task_func(list_of_menuitems) == expected_result

def test_task_func_single_item_list():
    list_of_menuitems = [
        ['a']
    ]
    expected_result = 'a'
    assert task_func(list_of_menuitems) == expected_result

def test_task_func_duplicate_items():
    list_of_menuitems = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        ['g', 'h', 'i']
    ]
    expected_result = 'e'
    assert task_func(list_of_menuitems) == expected_result

def test_task_func_duplicate_items_with_different_case():
    list_of_menuitems = [
        ['a', 'b', 'c'],
        ['d', 'E', 'f'],
        ['g', 'h', 'i']
    ]
    expected_result = 'E'
    assert task_func(list_of_menuitems) == expected_result