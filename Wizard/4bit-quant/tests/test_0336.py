python
import collections
from queue import PriorityQueue
import random
import pytest

# Constants
LETTERS = ['a', 'b', 'c', 'd', 'e']

def task_func(string_length=100):

    string = ''.join([LETTERS[random.randint(0, len(LETTERS)-1)] for _ in range(string_length)])

    freq = collections.Counter(string)

    pq = PriorityQueue()
    for letter, count in freq.items():
        pq.put((-count, letter))

    sorted_freq = collections.OrderedDict()
    while not pq.empty():
        count, letter = pq.get()
        sorted_freq[letter] = -count

    return sorted_freq

def test_task_func():
    # Test case 1
    assert task_func(10) == {'a': -1, 'b': -1, 'c': -1, 'd': -1, 'e': -1}

    # Test case 2
    assert task_func(5) == {'a': -1, 'b': -1, 'c': -1, 'd': -1, 'e': -1}

    # Test case 3
    assert task_func(100) == {'a': -1, 'b': -1, 'c': -1, 'd': -1, 'e': -1}

    # Test case 4
    assert task_func(0) == {}

    # Test case 5
    assert task_func(-10) == {}

    # Test case 6
    assert task_func(1000) == {'a': -1, 'b': -1, 'c': -1, 'd': -1, 'e': -1}

    # Test case 7
    assert task_func(10000) == {'a': -1, 'b': -1, 'c': -1, 'd': -1, 'e': -1}

    # Test case 8
    assert task_func(100000) == {'a': -1, 'b': -1, 'c': -1, 'd': -1, 'e': -1}

    # Test case 9
    assert task_func(1000000) == {'a': -1, 'b': -1, 'c': -1, 'd': -1, 'e': -1}

    # Test case 10
    assert task_func(10000000) == {'a': -1, 'b': -1, 'c': -1, 'd': -1, 'e': -1}