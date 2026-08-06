import pytest
from src_0547 import task_func
from collections import OrderedDict
from prettytable import PrettyTable

def test_task_func_with_empty_dict():
    my_dict = {}
    result = task_func(my_dict)
    expected_output = PrettyTable(['Key', 'Value'])
    assert str(result) == str(expected_output)

def test_task_func_with_single_item():
    my_dict = {'a': 1}
    result = task_func(my_dict)
    expected_output = PrettyTable(['Key', 'Value'])
    expected_output.add_row(['a', 1])
    assert str(result) == str(expected_output)

def test_task_func_with_multiple_items():
    my_dict = {'b': 2, 'a': 1, 'c': 3}
    result = task_func(my_dict)
    expected_output = PrettyTable(['Key', 'Value'])
    expected_output.add_row(['a', 1])
    expected_output.add_row(['b', 2])
    expected_output.add_row(['c', 3])
    assert str(result) == str(expected_output)

def test_task_func_with_same_values():
    my_dict = {'x': 10, 'y': 10, 'z': 10}
    result = task_func(my_dict)
    expected_output = PrettyTable(['Key', 'Value'])
    expected_output.add_row(['x', 10])
    expected_output.add_row(['y', 10])
    expected_output.add_row(['z', 10])
    assert str(result) == str(expected_output)

def test_task_func_with_numeric_keys():
    my_dict = {3: 'three', 1: 'one', 2: 'two'}
    result = task_func(my_dict)
    expected_output = PrettyTable(['Key', 'Value'])
    expected_output.add_row([1, 'one'])
    expected_output.add_row([2, 'two'])
    expected_output.add_row([3, 'three'])
    assert str(result) == str(expected_output)