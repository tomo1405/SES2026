import pytest
from collections import Counter
import heapq
# Constants
LETTERS = list('abcdefghijklmnopqrstuvwxyz')
def task_func(my_dict):
    letter_counter = Counter(my_dict)
    most_common_letters = heapq.nlargest(3, letter_counter, key=letter_counter.get)

    return most_common_letters
def test_task_func():
    my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    expected_result = [('e', 5), ('d', 4), ('c', 3)]
    result = task_func(my_dict)
    assert result == expected_result