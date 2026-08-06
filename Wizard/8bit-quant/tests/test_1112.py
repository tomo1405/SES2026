python
import pytest
from src_1112 import task_func

def test_task_func():
    animal_dict = {'cat': 2, 'dog': 1, 'elephant': 3, 'fox': 2, 'giraffe': 1, 'hippo': 1, 'iguana': 2, 'jaguar': 1}
    expected_result = {'a': 2, 'c': 1, 'd': 1, 'e': 3, 'f': 2, 'g': 1, 'h': 1, 'i': 2, 'j': 1}
    assert task_func(animal_dict) == expected_result