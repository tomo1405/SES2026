python
import collections
import random
import pytest
from src_0336 import task_func

LETTERS = ['a', 'b', 'c', 'd', 'e']

def test_task_func():
    string_length = 100
    string = ''.join([LETTERS[random.randint(0, len(LETTERS)-1)] for _ in range(string_length)])
    freq = collections.Counter(string)
    pq = PriorityQueue()
    for letter, count in freq.items():
        pq.put((-count, letter))
    sorted_freq = collections.OrderedDict()
    while not pq.empty():
        count, letter = pq.get()
        sorted_freq[letter] = -count
    assert task_func(string_length) == sorted_freq