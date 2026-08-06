import pytest
from collections import Counter
from random import choice, seed
from src_0862 import task_func
POSSIBLE_ITEMS = ['apple', 'banana', 'cherry', 'date', 'elderberry']

def test_task_func():
    list_of_lists = [[1, 2, 3], [4, 5, 6]]
    seed(42)  # Set the seed for reproducibility
    baskets = task_func(list_of_lists)
    assert isinstance(baskets, list)
    for basket in baskets:
        assert isinstance(basket, Counter)
        assert len(basket) == len(POSSIBLE_ITEMS)
        for item inPSSIBLE_ITEMS:
            assert basket[item] >= 0

def test_task_func_with_empty_list():
    list_of_lists = [[], []]
    seed(42)  # Set the seed for reproducibility
    baskets = task_func(list_of_lists)
    assert isinstance(baskets, list)
    for basket in baskets:
        assert isinstance(basket, Counter)
        assert len(basket) == len(POSSIBLE_ITEMS)
        for item inPSSIBLE_ITEMS:
            assert basket[item] == 0

def test_task_func_with_invalid_input():
    with pytest.raises(TypeError):
        task_func('invalid input')