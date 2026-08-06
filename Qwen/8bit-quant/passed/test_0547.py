import pytest
from src_0547 import task_func
from collections import OrderedDict
from prettytable import PrettyTable

def test_task_func_empty_dict():
    input_dict = {}
    expected_output = PrettyTable(['Key', 'Value'])
    result = task_func(input_dict)
    assert str(result) == str(expected_output)

def test_task_func_single_item():
    input_dict = {'a': 1}
    expected_output = PrettyTable(['Key', 'Value'])
    expected_output.add_row(['a', 1])
    result = task_func(input_dict)
    assert str(result) == str(expected_output)

def test_task_func_multiple_items_unordered():
    input_dict = {'b': 2, 'a': 1, 'c': 3}
    expected_output = PrettyTable(['Key', 'Value'])
    expected_output.add_row(['a', 1])
    expected_output.add_row(['b', 2])
    expected_output.add_row(['c', 3])
    result = task_func(input_dict)
    assert str(result) == str(expected_output)

def test_task_func_with_same_keys():
    input_dict = {'a': 1, 'a': 2}
    expected_output = PrettyTable(['Key', 'Value'])
    expected_output.add_row(['a', 2])
    result = task_func(input_dict)
    assert str(result) == str(expected_output)

def test_task_func_with_non_string_keys():
    input_dict = {1: 'one', 2: 'two', 3: 'three'}
    expected_output = PrettyTable(['Key', 'Value'])
    expected_output.add_row([1, 'one'])
    expected_output.add_row([2, 'two'])
    expected_output.add_row([3, 'three'])
    result = task_func(input_dict)
    assert str(result) == str(expected_output)