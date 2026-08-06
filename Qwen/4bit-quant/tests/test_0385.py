import collections

import pytest
from src_0385 import task_func

# Test cases for the task_func function

def test_task_func_with_default_values():
    animal_dict = {'a': 'Cat', 'b': 'Dog', 'c': 'Elephant'}
    expected_reversed_dict = {'Cat': ['a'], 'Dog': ['b'], 'Elephant': ['c']}
    expected_animal_counter = collections.Counter({'Cat': 1, 'Dog': 1, 'Elephant': 1})
    
    reversed_dict, animal_counter = task_func(animal_dict)
    assert reversed_dict == expected_reversed_dict
    assert animal_counter == expected_animal_counter

def test_task_func_with_max_count_greater_than_default():
    animal_dict = {'x': 'Lion', 'y': 'Tiger', 'z': 'Bear'}
    max_count = 20
    expected_reversed_dict = {'Lion': ['x'], 'Tiger': ['y'], 'Bear': ['z']}
    expected_animal_counter = collections.Counter({'Lion': 1, 'Tiger': 1, 'Bear': 1})
    
    reversed_dict, animal_counter = task_func(animal_dict, max_count=max_count)
    assert reversed_dict == expected_reversed_dict
    assert animal_counter == expected_animal_counter

def test_task_func_with_different_seed():
    animal_dict = {'m': 'Giraffe', 'n': 'Horse', 'o': 'Rabbit'}
    seed = 42
    expected_reversed_dict = {'Giraffe': ['m'], 'Horse': ['n'], 'Rabbit': ['o']}
    expected_animal_counter = collections.Counter({'Giraffe': 1, 'Horse': 1, 'Rabbit': 1})
    
    reversed_dict, animal_counter = task_func(animal_dict, seed=seed)
    assert reversed_dict == expected_reversed_dict
    assert animal_counter == expected_animal_counter

def test_task_func_with_non_animal_values():
    animal_dict = {'p': 'Fish', 'q': 'Monkey', 'r': 'Cat'}
    expected_reversed_dict = {'Cat': ['r']}
    expected_animal_counter = collections.Counter({'Cat': 1})
    
    reversed_dict, animal_counter = task_func(animal_dict)
    assert reversed_dict == expected_reversed_dict
    assert animal_counter == expected_animal_counter

def test_task_func_with_empty_dict():
    animal_dict = {}
    expected_reversed_dict = {}
    expected_animal_counter = collections.Counter()
    
    reversed_dict, animal_counter = task_func(animal_dict)
    assert reversed_dict == expected_reversed_dict
    assert animal_counter == expected_animal_counter

def test_task_func_with_max_count_less_than_one():
    with pytest.raises(ValueError):
        task_func({'s': 'Snake'}, max_count=0)

def test_task_func_with_non_string_values():
    animal_dict = {'t': 123, 'u': 'Zebra', 'v': None}
    expected_reversed_dict = {'Zebra': ['u']}
    expected_animal_counter = collections.Counter({'Zebra': 1})
    
    reversed_dict, animal_counter = task_func(animal_dict)
    assert reversed_dict == expected_reversed_dict
    assert animal_counter == expected_animal_counter