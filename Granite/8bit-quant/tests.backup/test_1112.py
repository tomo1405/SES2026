import pytest
from src_1112 import task_func

def test_task_func():
    animal_dict = {'cat': 1, 'dog': 2, 'elephant': 3, 'fox': 4, 'giraffe': 5, 'hippo': 6, 'iguana': 7, 'jaguar': 8}
    expected_result = {'a': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1, 'l': 2, 'n': 2, 'o': 2, 'p': 2, 'r': 2, 's': 2, 't': 2, 'u': 1, 'v': 1, 'y': 1}
    result = task_func(animal_dict)
    assert result == expected_result

def test_task_func_with_empty_dict():
    animal_dict = {}
    expected_result = {}
    result = task_func(animal_dict)
    assert result == expected_result

def test_task_func_with_non_dict_input():
    animal_dict = 'not a dictionary'
    with pytest.raises(TypeError) as excinfo:
        task_func(animal_dict)
    assert "Input must be a dictionary" in str(excinfo.value)