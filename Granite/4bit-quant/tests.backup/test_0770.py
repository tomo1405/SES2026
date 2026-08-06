import pytest
from collections import Counter
import itertools
import operator

def task_func(list_of_menuitems):
    flat_list = list(itertools.chain(*list_of_menuitems))

    counter = Counter(flat_list)

    return max(counter.items(), key=operator.itemgetter(1))[0]

def test_task_func():
    list_of_menuitems = [['a', 'b', 'c'], ['d', 'e', 'f']]
    expected_output = 'a'
    actual_output = task_func(list_of_menuitems)
    assert actual_output == expected_output, "Test case 1 failed"

    list_of_menuitems = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
    expected_output = 'a'
    actual_output = task_func(list_of_menuitems)
    assert actual_output == expected_output, "Test case 2 failed"

    list_of_menuitems = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l']]
    expected_output = 'a'
    actual_output = task_func(list_of_menuitems)
    assert actual_output == expected_output, "Test case 3 failed"

if __name__ == "__main__":
    pytest.main()