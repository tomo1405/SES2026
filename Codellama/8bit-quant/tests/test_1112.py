import pytest
from src_1112 import task_func

def test_task_func():
    animal_dict = {'cat': 2, 'dog': 3, 'elephant': 1, 'fox': 1, 'giraffe': 2, 'hippo': 1, 'iguana': 1, 'jaguar': 1}
    expected_result = {'g': 2, 'd': 2, 'c': 2, 'e': 1, 'f': 1, 'h': 1, 'i': 1, 'j': 1}
    assert task_func(animal_dict) == expected_result