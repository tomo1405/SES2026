import pytest
from src_0727 import task_func

def test_task_func():
    s = "This is a sample sentence with some English words like cat and dog."
    n = 2
    expected_output = ['cat', 'dog']
    actual_output = task_func(s, n)
    assert actual_output == expected_output, "Output does not match expected output"

def test_task_func_with_less_english_words():
    s = "This sentence has only two words, neither of which are English."
    n = 5
    expected_output = ['two', 'words']
    actual_output = task_func(s, n)
    assert actual_output == expected_output, "Output does not match expected output"

def test_task_func_with_no_english_words():
    s = "This sentence has no English words at all."
    n = 3
    expected_output = []
    actual_output = task_func(s, n)
    assert actual_output == expected_output, "Output does not match expected output"