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
    list_of_menuitems = [["item1", "item2", "item3"], ["item4", "item5", "item6"]]
    assert task_func(list_of_menuitems) == "item3"

    # Test case 2
    list_of_menuitems = [["item1", "item2", "item3"], ["item4", "item5", "item6"], ["item7", "item8", "item9"]]
    assert task_func(list_of_menuitems) == "item9"

    # Test case 3
    list_of_menuitems = [["item1", "item2", "item3"], ["item4", "item5", "item6"], ["item7", "item8", "item9"], ["item10", "item11", "item12"]]
    assert task_func(list_of_menuitems) == "item12"

    # Test case 4
    list_of_menuitems = [["item1", "item2", "item3"], ["item4", "item5", "item6"], ["item7", "item8", "item9"], ["item10", "item11", "item12"], ["item13", "item14", "item15"]]
    assert task_func(list_of_menuitems) == "item15"

    # Test case 5
    list_of_menuitems = [["item1", "item2", "item3"], ["item4", "item5", "item6"], ["item7", "item8", "item9"], ["item10", "item11", "item12"], ["item13", "item14", "item15"], ["item16", "item17", "item18"]]
    assert task_func(list_of_menuitems) == "item18"

    # Test case 6
    list_of_menuitems = [["item1", "item2", "item3"], ["item4", "item5", "item6"], ["item7", "item8", "item9"], ["item10", "item11", "item12"], ["item13", "item14", "item15"], ["item16", "item17", "item18"], ["item19", "item20", "item21"]]
    assert task_func(list_of_menuitems) == "item21"

    # Test case 7
    list_of_menuitems = [["item1", "item2", "item3"], ["item4", "item5", "item6"], ["item7", "item8", "item9"], ["item10", "item11", "item12"], ["item13", "item14", "item15"], ["item16", "item17", "item18"], ["item19", "item20", "item21"], ["item22", "item23", "item24"]]
    assert task_func(list_of_menuitems) == "item24"

    # Test case 8
    list_of_menuitems = [["item1", "item2", "item3"], ["item4", "item5", "item6"], ["item7", "item8", "item9"], ["item10", "item11", "item12"], ["item13", "item14", "item15"], ["item16", "item17", "item18"], ["item19", "item20", "item21"], ["item22", "item23", "item24"], ["item25", "item26", "item27"]]
    assert task_func(list_of_menuitems) == "item27"

    # Test case 9
    list_of_menuitems = [["item1", "item2", "item3"], ["item4", "item5", "item6"], ["item7", "item8", "item9"], ["item10", "item11", "item12"], ["item13", "item14", "item15"], ["item16", "item17", "item18"], ["item19", "item20", "item21"], ["item22", "item23", "item24"], ["item25", "item26", "item27"], ["item28", "item29", "item30"]]
    assert task_func(list_of_menuitems) == "item30"

    # Test case 10
    list_of_menuitems = [["item1", "item2", "item3"], ["item4", "item5", "item6"], ["item7", "item8", "item9"], ["item10", "item11", "item12"], ["item13", "item14", "item15"], ["item16", "item17", "item18"], ["item19", "item20", "item21"], ["item22", "item23", "item24"], ["item25", "item26", "item27"], ["item28", "item29", "item30"], ["item31", "item32", "item33"]]
    assert task_func(list_of_menuitems) == "item33"