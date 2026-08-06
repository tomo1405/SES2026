python
import pytest
from src_1112 import task_func

def test_task_func():
    animal_dict = {'cat': 2, 'camel': 1, 'dog': 3, 'elephant': 4, 'fox': 5, 'giraffe': 6, 'hippo': 7, 'iguana': 8, 'jaguar': 9}
    expected_result = {'a': 2, 'c': 1, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9}
    assert task_func(animal_dict) == expected_result