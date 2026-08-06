python
import pytest
from src_1112 import task_func

def test_task_func():
    animal_dict = {'cat': 2, 'dog': 3, 'elephant': 1, 'fox': 4, 'giraffe': 5, 'hippo': 6, 'iguana': 7, 'jaguar': 8}
    expected_result = {'a': 2, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1, 'l': 1, 'n': 1, 'o': 1, 'r': 1, 't': 1, 'u': 1, 'w': 1}
    assert task_func(animal_dict) == expected_result