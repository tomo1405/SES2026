import pytest
from src_0667 import task_func

def test_task_func():
    seq = 'ABCD'
    letter_weight_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
    expected_output = 'ABCD'

    actual_output = task_func(seq, letter_weight_dict)

    assert actual_output == expected_output, "Output does not match expected output"

def test_task_func_with_different_input():
    seq = 'ABCD'
    letter_weight_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
    expected_output = 'ACBD'

    actual_output = task_func(seq, letter_weight_dict)

    assert actual_output == expected_output, "Output does not match expected output"