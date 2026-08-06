import pytest
from src_0385 import task_func

def test_task_func_valid_input():
    animal_dict = {'cat': 'Cat', 'dog': 'Dog', 'elephant': 'Elephant', 'lion': 'Lion', 'tiger': 'Tiger', 'bear': 'Bear', 'giraffe': 'Giraffe', 'horse': 'Horse', 'rabbit': 'Rabbit', 'snake': 'Snake', 'zebra': 'Zebra'}
    reversed_dict, animal_counter = task_func(animal_dict)
    assert reversed_dict == {'Cat': ['cat'], 'Dog': ['dog'], 'Elephant': ['elephant'], 'Lion': ['lion'], 'Tiger': ['tiger'], 'Bear': ['bear'], 'Giraffe': ['giraffe'], 'Horse': ['horse'], 'Rabbit': ['rabbit'], 'Snake': ['snake'], 'Zebra': ['zebra']}
    assert animal_counter == {'Cat': 1, 'Dog': 1, 'Elephant': 1, 'Lion': 1, 'Tiger': 1, 'Bear': 1, 'Giraffe': 1, 'Horse': 1, 'Rabbit': 1, 'Snake': 1, 'Zebra': 1}

def test_task_func_invalid_input():
    animal_dict = {'cat': 'Cat', 'dog': 'Dog', 'elephant': 'Elephant', 'lion': 'Lion', 'tiger': 'Tiger', 'bear': 'Bear', 'giraffe': 'Giraffe', 'horse': 'Horse', 'rabbit': 'Rabbit', 'snake': 'Snake', 'zebra': 'Zebra'}
    with pytest.raises(ValueError):
        task_func(animal_dict, max_count=0)

def test_task_func_random_input():
    animal_dict = {'cat': 'Cat', 'dog': 'Dog', 'elephant': 'Elephant', 'lion': 'Lion', 'tiger': 'Tiger', 'bear': 'Bear', 'giraffe': 'Giraffe', 'horse': 'Horse', 'rabbit': 'Rabbit', 'snake': 'Snake', 'zebra': 'Zebra'}
    reversed_dict, animal_counter = task_func(animal_dict, seed=42)
    assert reversed_dict == {'Cat': ['cat'], 'Dog': ['dog'], 'Elephant': ['elephant'], 'Lion': ['lion'], 'Tiger': ['tiger'], 'Bear': ['bear'], 'Giraffe': ['giraffe'], 'Horse': ['horse'], 'Rabbit': ['rabbit'], 'Snake': ['snake'], 'Zebra': ['zebra']}
    assert animal_counter == {'Cat': 1, 'Dog': 1, 'Elephant': 1, 'Lion': 1, 'Tiger': 1, 'Bear': 1, 'Giraffe': 1, 'Horse': 1, 'Rabbit': 1, 'Snake': 1, 'Zebra': 1}