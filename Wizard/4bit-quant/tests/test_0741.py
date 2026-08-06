python
import heapq
from collections import Counter

LETTERS = list('abcdefghijklmnopqrstuvwxyz')

def task_func(my_dict):
    letter_counter = Counter(my_dict)
    most_common_letters = heapq.nlargest(3, letter_counter, key=letter_counter.get)

    return most_common_letters

def test_task_func():
    my_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
    assert task_func(my_dict) == ['e', 'd', 'c']

    my_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50, 'f': 60, 'g': 70}
    assert task_func(my_dict) == ['g', 'f', 'e']

    my_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50, 'f': 60, 'g': 70, 'h': 80, 'i': 90, 'j': 100}
    assert task_func(my_dict) == ['j', 'i', 'h']