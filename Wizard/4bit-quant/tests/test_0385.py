python
import collections
import random
import itertools
import pytest

from src_0385 import task_func

ANIMALS = ['Cat', 'Dog', 'Elephant', 'Lion', 'Tiger', 'Bear', 'Giraffe', 'Horse', 'Rabbit', 'Snake', 'Zebra']

def test_task_func():
    animal_dict = {'A': 'Cat', 'B': 'Dog', 'C': 'Elephant', 'D': 'Lion', 'E': 'Tiger', 'F': 'Bear', 'G': 'Giraffe', 'H': 'Horse', 'I': 'Rabbit', 'J': 'Snake', 'K': 'Zebra'}
    max_count = 10
    seed = 0

    reversed_dict, animal_counter = task_func(animal_dict, max_count, seed)

    assert isinstance(reversed_dict, dict)
    assert isinstance(animal_counter, collections.Counter)

    for k, v in reversed_dict.items():
        assert isinstance(k, str)
        assert k in ANIMALS
        assert isinstance(v, list)
        assert all(isinstance(i, str) for i in v)

    for k, v in animal_counter.items():
        assert k in ANIMALS
        assert isinstance(v, int)
        assert v >= 1
        assert v <= max_count