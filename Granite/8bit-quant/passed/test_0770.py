import pytest
from collections import Counter
import itertools
import operator

def task_func(list_of_menuitems):
    flat_list = list(itertools.chain(*list_of_menuitems))

    counter = Counter(flat_list)

    return max(counter.items(), key=operator.itemgetter(1))[0]

def test_task_func():
    list_of_menuitems = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
    expected_output = 'a'
    actual_output = task_func(list_of_menuitems)
    assert actual_output == expected_output, "Expected output does not match actual output"

def test_task_func_with_empty_list():
    list_of_menuitems = [[], [], []]
    with pytest.raises(ValueError):
        task_func(list_of_menuitems)

def test_task_func_with_list_of_lists_with_different_lengths():
    list_of_menuitems = [['a', 'b', 'c'], ['d', 'e'], ['f', 'g', 'h', 'i']]
    with pytest.raises(ValueError):
        task_func(list_of_menuitems)