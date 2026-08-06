import pytest
from functools import reduce
import operator
import string

def task_func(letters):
    letter_to_number = {letter: i+1 for i, letter in enumerate(string.ascii_uppercase)}
    numbers = [letter_to_number[letter] for letter in letters]
    product = reduce(operator.mul, numbers, 1)
    return product

def test_task_func():
    assert task_func(['A', 'B', 'C']) == 6
    assert task_func(['A', 'B', 'C', 'D']) == 24
    assert task_func(['A']) == 1
    with pytest.raises(KeyError):
        task_func(['Z'])