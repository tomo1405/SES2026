import pytest
from src_0385 import task_func

def test_task_func():
    animal_dict = {'a': 'Cat', 'b': 'Dog', 'c': 'Elephant', 'd': 'Lion', 'e': 'Tiger', 'f': 'Bear', 'g': 'Giraffe', 'h': 'Horse', 'i': 'Rabbit', 'j': 'Snake', 'k': 'Zebra'}
    max_count = 10
    seed = 0
    reversed_dict, animal_counter = task_func(animal_dict, max_count, seed)
    assert isinstance(reversed_dict, dict)
    assert all(isinstance(k, str) and isinstance(v, list) for k, v in reversed_dict.items())
    assert all(v in ANIMALS for v in reversed_dict.keys())
    assert all(isinstance(k, str) and isinstance(v, int) for k, v in animal_counter.items())
    assert all(v <= max_count for v in animal_counter.values())

def test_task_func_invalid_max_count():
    animal_dict = {'a': 'Cat', 'b': 'Dog', 'c': 'Elephant', 'd': 'Lion', 'e': 'Tiger', 'f': 'Bear', 'g': 'Giraffe', 'h': 'Horse', 'i': 'Rabbit', 'j': 'Snake', 'k': 'Zebra'}
    max_count = 0
    seed = 0
    with pytest.raises(ValueError):
        task_func(animal_dict, max_count, seed)