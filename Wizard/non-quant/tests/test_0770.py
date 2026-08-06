python
import itertools
import operator
from collections import Counter

def task_func(list_of_menuitems):
    flat_list = list(itertools.chain(*list_of_menuitems))

    counter = Counter(flat_list)

    return max(counter.items(), key=operator.itemgetter(1))[0]

def test_task_func():
    # Test case 1
    list_of_menuitems = [["item1", "item2", "item3"], ["item2", "item3", "item4"], ["item3", "item4", "item5"]]
    expected_result = "item3"
    assert task_func(list_of_menuitems) == expected_result

    # Test case 2
    list_of_menuitems = [["item1", "item2", "item3"], ["item2", "item3", "item4"], ["item3", "item4", "item5", "item6"]]
    expected_result = "item6"
    assert task_func(list_of_menuitems) == expected_result

    # Test case 3
    list_of_menuitems = [["item1", "item2", "item3"], ["item2", "item3", "item4"], ["item3", "item4", "item5", "item6", "item7"]]
    expected_result = "item7"
    assert task_func(list_of_menuitems) == expected_result