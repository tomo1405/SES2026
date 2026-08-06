python
import pytest
from src_0667 import task_func

def test_task_func():
    seq = 'abcde'
    letter_weight_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    expected_result = 'abc'
    assert task_func(seq, letter_weight_dict) == expected_result