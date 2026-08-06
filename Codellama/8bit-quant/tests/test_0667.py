import pytest
from src_0667 import task_func

def test_task_func():
    seq = 'abcd'
    letter_weight_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    expected_subseq = 'abcd'
    expected_weight = 10

    subseq, weight = task_func(seq, letter_weight_dict)

    assert subseq == expected_subseq
    assert weight == expected_weight