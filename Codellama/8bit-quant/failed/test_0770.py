import pytest
from src_0770 import task_func

def test_task_func():
    list_of_menuitems = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        ['g', 'h', 'i']
    ]
    expected_result = 'e'

    result = task_func(list_of_menuitems)

    assert result == expected_result