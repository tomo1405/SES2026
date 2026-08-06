import pytest
from collections import OrderedDict
from prettytable import PrettyTable

def task_func(my_dict):
    ordered_dict = OrderedDict(sorted(my_dict.items(), key=lambda t: t[0]))
    table = PrettyTable(['Key', 'Value'])

    for key, value in ordered_dict.items():
        table.add_row([key, value])

    return table

def test_task_func():
    my_dict = {'b': 2, 'a': 1, 'c': 3}
    expected_table = PrettyTable(['Key', 'Value'])
    expected_table.add_row(['a', 1])
    expected_table.add_row(['b', 2])
    expected_table.add_row(['c', 3])

    actual_table = task_func(my_dict)

    assert actual_table == expected_table