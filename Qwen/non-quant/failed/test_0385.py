import pytest
from src_0385 import task_func

# Define the expected results for the test cases
def test_task_func_with_default_parameters():
    animal_dict = {'a': 'Cat', 'b': 'Dog', 'c': 'Elephant', 'd': 'Lion', 'e': 'Tiger'}
    reversed_dict, animal_counter = task_func(animal_dict)
    assert reversed_dict == {
        'Cat': ['a'],
        'Dog': ['b'],
        'Elephant': ['c'],
        'Lion': ['d'],
        'Tiger': ['e']
    }
    assert all(isinstance(count, int) for count in animal_counter.values())

def test_task_func_with_custom_max_count():
    animal_dict = {'a': 'Cat', 'b': 'Dog', 'c': 'Elephant', 'd': 'Lion', 'e': 'Tiger'}
    reversed_dict, animal_counter = task_func(animal_dict, max_count=5)
    assert reversed_dict == {
        'Cat': ['a'],
        'Dog': ['b'],
        'Elephant': ['c'],
        'Lion': ['d'],
        'Tiger': ['e']
    }
    assert all(1 <= count <= 5 for count in animal_counter.values())

def test_task_func_with_custom_seed():
    animal_dict = {'a': 'Cat', 'b': 'Dog', 'c': 'Elephant', 'd': 'Lion', 'e': 'Tiger'}
    reversed_dict, animal_counter = task_func(animal_dict, seed=42)
    assert reversed_dict == {
        'Cat': ['a'],
        'Dog': ['b'],
        'Elephant': ['c'],
        'Lion': ['d'],
        'Tiger': ['e']
    }
    assert animal_counter == collections.Counter({'Cat': 3, 'Dog': 3, 'Elephant': 3, 'Lion': 3, 'Tiger': 3, 'Bear': 2, 'Giraffe': 2, 'Horse': 2, 'Rabbit': 2, 'Snake': 2, 'Zebra': 2})

def test_task_func_with_non_animal_values():
    animal_dict = {'a': 'Cat', 'b': 'Fish', 'c': 'Elephant', 'd': 'Lion', 'e': 'Tiger'}
    reversed_dict, animal_counter = task_func(animal_dict)
    assert reversed_dict == {
        'Cat': ['a'],
        'Elephant': ['c'],
        'Lion': ['d'],
        'Tiger': ['e']
    }
    assert all(isinstance(count, int) for count in animal_counter.values())

def test_task_func_with_empty_dict():
    animal_dict = {}
    reversed_dict, animal_counter = task_func(animal_dict)
    assert reversed_dict == {}
    assert animal_counter == collections.Counter()

def test_task_func_with_invalid_max_count():
    with pytest.raises(ValueError):
        task_func({'a': 'Cat'}, max_count=0)

def test_task_func_with_invalid_animal_value():
    animal_dict = {'a': 'Cat', 'b': 'Dragon'}
    reversed_dict, animal_counter = task_func(animal_dict)
    assert reversed_dict == {'Cat': ['a']}
    assert all(isinstance(count, int) for count in animal_counter.values())