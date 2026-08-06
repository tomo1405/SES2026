import pytest
from src_1112 import task_func

def test_task_func():
    animal_dict = {'cat': 1, 'dog': 2, 'elephant': 3, 'fox': 4, 'giraffe': 5, 'hippo': 6, 'iguana': 7, 'jaguar': 8}
    expected_result = {'e': 3, 'a': 2, 'g': 2, 'o': 2, 'i': 2, 'p': 2, 'h': 2, 'n': 2, 'd': 2, 'f': 2, 'x': 2, 'c': 2, 'j': 2, 'u': 2, 's': 2, 't': 2, 'r': 2, 'l': 2, 'b': 2, 'y': 2, 'm': 2, 'w': 2, 'v': 2, 'k': 2, 'q': 2, 'z': 2}
    assert task_func(animal_dict) == expected_result