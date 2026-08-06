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

    assert reversed_dict == {'Cat': ['A'], 'Dog': ['B'], 'Elephant': ['C'], 'Lion': ['D'], 'Tiger': ['E'], 'Bear': ['F'], 'Giraffe': ['G'], 'Horse': ['H'], 'Rabbit': ['I'], 'Snake': ['J'], 'Zebra': ['K']}
    assert animal_counter == {'Cat': 1, 'Dog': 1, 'Elephant': 1, 'Lion': 1, 'Tiger': 1, 'Bear': 1, 'Giraffe': 1, 'Horse': 1, 'Rabbit': 1, 'Snake': 1, 'Zebra': 1}

    animal_dict = {'A': 'Cat', 'B': 'Dog', 'C': 'Elephant', 'D': 'Lion', 'E': 'Tiger', 'F': 'Bear', 'G': 'Giraffe', 'H': 'Horse', 'I': 'Rabbit', 'J': 'Snake', 'K': 'Zebra'}
    max_count = 5
    seed = 0

    reversed_dict, animal_counter = task_func(animal_dict, max_count, seed)

    assert reversed_dict == {'Cat': ['A'], 'Dog': ['B'], 'Elephant': ['C'], 'Lion': ['D'], 'Tiger': ['E'], 'Bear': ['F'], 'Giraffe': ['G'], 'Horse': ['H'], 'Rabbit': ['I'], 'Snake': ['J'], 'Zebra': ['K']}
    assert animal_counter == {'Cat': 1, 'Dog': 1, 'Elephant': 1, 'Lion': 1, 'Tiger': 1, 'Bear': 1, 'Giraffe': 1, 'Horse': 1, 'Rabbit': 1, 'Snake': 1, 'Zebra': 1}

    animal_dict = {'A': 'Cat', 'B': 'Dog', 'C': 'Elephant', 'D': 'Lion', 'E': 'Tiger', 'F': 'Bear', 'G': 'Giraffe', 'H': 'Horse', 'I': 'Rabbit', 'J': 'Snake', 'K': 'Zebra'}
    max_count = 0
    seed = 0

    with pytest.raises(ValueError):
        reversed_dict, animal_counter = task_func(animal_dict, max_count, seed)