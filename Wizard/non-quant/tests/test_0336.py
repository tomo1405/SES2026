python
import collections
import random
import pytest

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
    assert task_func() == collections.OrderedDict({'a': -1, 'b': -1, 'c': -1, 'd': -1, 'e': -1})
    assert task_func(string_length=5) == collections.OrderedDict({'a': -1, 'b': -1, 'c': -1, 'd': -1, 'e': -1})
    assert task_func(string_length=10) == collections.OrderedDict({'a': -1, 'b': -1, 'c': -1, 'd': -1, 'e': -1})
    assert task_func(string_length=100) == collections.OrderedDict({'a': -1, 'b': -1, 'c': -1, 'd': -1, 'e': -1})
    assert task_func(string_length=1000) == collections.OrderedDict({'a': -1, 'b': -1, 'c': -1, 'd': -1, 'e': -1})
    assert task_func(string_length=10000) == collections.OrderedDict({'a': -1, 'b': -1, 'c': -1, 'd': -1, 'e': -1})
    assert task_func(string_length=100000) == collections.OrderedDict({'a': -1, 'b': -1, 'c': -1, 'd': -1, 'e': -1})
    assert task_func(string_length=1000000) == collections.OrderedDict({'a': -1, 'b': -1, 'c': -1, 'd': -1, 'e': -1})