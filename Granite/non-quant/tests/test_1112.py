import pytest
from collections import Counter
from operator import itemgetter
import itertools
from src_1112 import task_func

#CONSTANT
ANIMAL = ['cat', 'camel', 'cow', 'dog', 'elephant', 'fox', 'giraffe', 'hippo', 'iguana', 'jaguar']

def test_task_func():
    animal_dict = {'cat': 1, 'dog': 2, 'cow': 3}
    expected_result = {'a': 1, 'c': 1, 'd': 1, 'e': 1, 'g': 1, 'h': 1, 'i': 1, 'o': 2, 'r': 1, 't': 1}
    assert task_func(animal_dict) == expected_result

def test_task_func_with_empty_dict():
    animal_dict = {}
    expected_result = {}
    assert task_func(animal_dict) == expected_result

def test_task_func_with_invalid_input():
    animal_dict = 'invalid input'
    with pytest.raises(TypeError):
        task_func(animal_dict)