import pytest
from src_0385 import task_func

def test_task_func():
    animal_dict = {'cat': 'Cat', 'dog': 'Dog', 'elephant': 'Elephant'}
    reversed_dict, animal_counter = task_func(animal_dict)
    assert reversed_dict == {'Cat': ['cat'], 'Dog': ['dog'], 'Elephant': ['elephant']}
    assert animal_counter == {'Cat': 1, 'Dog': 1, 'Elephant': 1}

def test_task_func_with_max_count():
    animal_dict = {'cat': 'Cat', 'dog': 'Dog', 'elephant': 'Elephant'}
    reversed_dict, animal_counter = task_func(animal_dict, max_count=5)
    assert reversed_dict == {'Cat': ['cat'], 'Dog': ['dog'], 'Elephant': ['elephant']}
    assert animal_counter == {'Cat': 5, 'Dog': 5, 'Elephant': 5}

def test_task_func_with_seed():
    animal_dict = {'cat': 'Cat', 'dog': 'Dog', 'elephant': 'Elephant'}
    reversed_dict, animal_counter = task_func(animal_dict, seed=123)
    assert reversed_dict == {'Cat': ['cat'], 'Dog': ['dog'], 'Elephant': ['elephant']}
    assert animal_counter == {'Cat': 1, 'Dog': 1, 'Elephant': 1}

def test_task_func_with_invalid_max_count():
    animal_dict = {'cat': 'Cat', 'dog': 'Dog', 'elephant': 'Elephant'}
    with pytest.raises(ValueError):
        task_func(animal_dict, max_count=0)

def test_task_func_with_invalid_seed():
    animal_dict = {'cat': 'Cat', 'dog': 'Dog', 'elephant': 'Elephant'}
    with pytest.raises(ValueError):
        task_func(animal_dict, seed='abc')