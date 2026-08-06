import pytest
from src_0385 import task_func


def test_task_func_basic():
    animal_dict = {'a': 'Cat', 'b': 'Dog', 'c': 'Fish'}
    reversed_dict, animal_counter = task_func(animal_dict)
    assert reversed_dict == {'Cat': ['a'], 'Dog': ['b']}
    assert set(animal_counter.keys()) <= set(['Cat', 'Dog', 'Elephant', 'Lion', 'Tiger', 'Bear', 'Giraffe', 'Horse', 'Rabbit', 'Snake', 'Zebra'])

def test_task_func_max_count_zero():
    with pytest.raises(ValueError):
        task_func({'a': 'Cat'}, max_count=0)

def test_task_func_max_count_negative():
    with pytest.raises(ValueError):
        task_func({'a': 'Cat'}, max_count=-1)

def test_task_func_no_animals():
    animal_dict = {'a': 'Fish', 'b': 'Bird'}
    reversed_dict, animal_counter = task_func(animal_dict)
    assert reversed_dict == {}
    assert set(animal_counter.keys()) == set(['Cat', 'Dog', 'Elephant', 'Lion', 'Tiger', 'Bear', 'Giraffe', 'Horse', 'Rabbit', 'Snake', 'Zebra'])

def test_task_func_seed():
    animal_dict = {'a': 'Cat', 'b': 'Dog'}
    _, animal_counter_1 = task_func(animal_dict, seed=0)
    _, animal_counter_2 = task_func(animal_dict, seed=0)
    assert animal_counter_1 == animal_counter_2

def test_task_func_all_animals():
    animal_dict = {str(i): animal for i, animal in enumerate(ANIMALS)}
    reversed_dict, _ = task_func(animal_dict)
    assert reversed_dict == {animal: [str(i)] for i, animal in enumerate(ANIMALS)}

def test_task_func_non_string_values():
    animal_dict = {'a': 1, 'b': 'Cat', 'c': None}
    reversed_dict, _ = task_func(animal_dict)
    assert reversed_dict == {'Cat': ['b']}