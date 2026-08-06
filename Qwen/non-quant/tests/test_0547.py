import pytest
from src_0547 import task_func
from collections import OrderedDict
from prettytable import PrettyTable

def test_task_func_with_empty_dict():
    my_dict = {}
    expected_output = PrettyTable(['Key', 'Value'])
    assert str(task_func(my_dict)) == str(expected_output)

def test_task_func_with_single_item():
    my_dict = {'a': 1}
    expected_output = PrettyTable(['Key', 'Value'])
    expected_output.add_row(['a', 1])
    assert str(task_func(my_dict)) == str(expected_output)

def test_task_func_with_multiple_items():
    my_dict = {'b': 2, 'a': 1, 'c': 3}
    expected_output = PrettyTable(['Key', 'Value'])
    expected_output.add_row(['a', 1])
    expected_output.add_row(['b', 2])
    expected_output.add_row(['c', 3])
    assert str(task_func(my_dict)) == str(expected_output)

def test_task_func_with_string_keys():
    my_dict = {'apple': 1, 'banana': 2, 'cherry': 3}
    expected_output = PrettyTable(['Key', 'Value'])
    expected_output.add_row(['apple', 1])
    expected_output.add_row(['banana', 2])
    expected_output.add_row(['cherry', 3])
    assert str(task_func(my_dict)) == str(expected_output)

def test_task_func_with_mixed_key_types():
    my_dict = {1: 'one', 'two': 2, 3.0: 'three'}
    expected_output = PrettyTable(['Key', 'Value'])
    expected_output.add_row([1, 'one'])
    expected_output.add_row([3.0, 'three'])
    expected_output.add_row(['two', 2])
    assert str(task_func(my_dict)) == str(expected_output)