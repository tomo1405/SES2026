import pytest
from collections import Counter
from random import choice, seed
POSSIBLE_ITEMS = ['apple', 'banana', 'cherry', 'date', 'elderberry']
def task_func(list_of_lists):
    seed(42)  # Set the seed for reproducibility
    baskets = []
    for list_ in list_of_lists:
        basket = Counter()
        for _ in list_:
            basket[choice(POSSIBLE_ITEMS)] += 1
        baskets.append(basket)

    return baskets

def test_task_func():
    list_of_lists = [[1, 2, 3], [4, 5, 6]]
    expected_output = [Counter({'banana': 2, 'apple': 1, 'cherry': 1, 'date': 1, 'elderberry': 1}), 
                       Counter({'banana': 2, 'apple': 1, 'cherry': 1, 'date': 1, 'elderberry': 1})]
    actual_output = task_func(list_of_lists)
    assert actual_output == expected_output, "Output does not match expected output"

def test_task_func_with_empty_list():
    list_of_lists = [[], [4, 5, 6]]
    expected_output = [Counter(), Counter({'banana': 2, 'apple': 1, 'cherry': 1, 'date': 1, 'elderberry': 1})]
    actual_output = task_func(list_of_lists)
    assert actual_output == expected_output, "Output does not match expected output"

def test_task_func_with_invalid_input():
    with pytest.raises(TypeError):
        task_func('invalid input')