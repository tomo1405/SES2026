import pytest
from collections import Counter
from operator import itemgetter
import itertools
#CONSTANT
ANIMAL = ['cat', 'camel', 'cow', 'dog', 'elephant', 'fox', 'giraffe', 'hippo', 'iguana', 'jaguar']
def task_func(animal_dict):
    animal_dict_copy = {}
    for i in animal_dict:
        if i in ANIMAL:
            animal_dict_copy[i] = animal_dict[i]
    letters = list(itertools.chain.from_iterable(animal_dict_copy.keys()))
    count_dict = dict(Counter(letters))
    
    sorted_dict = dict(sorted(count_dict.items(), key=itemgetter(1), reverse=True))
    
    return sorted_dict

def test_task_func():
    animal_dict = {'cat': 1, 'dog': 2, 'cow': 3, 'hippo': 4, 'elephant': 5}
    expected_result = {'c': 3, 'a': 2, 't': 1, 'd': 1, 'o': 2, 'w': 1, 'h': 1, 'p': 1, 'e': 1, 'l': 1, 'f': 1, 'g': 1, 'j': 1}
    result = task_func(animal_dict)
    assert result == expected_result

def test_task_func_with_invalid_input():
    animal_dict = {'lion': 1, 'tiger': 2, 'monkey': 3, 'zebra': 4, 'giraffe': 5}
    with pytest.raises(KeyError):
        task_func(animal_dict)