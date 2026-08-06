import pytest
from src_0850 import task_func

def test_task_func():
    input_string = "This is a test\nThis is only a test\nThis is just a test"
    expected_output = {'This': 3, 'is': 3, 'only': 1, 'a': 2, 'test': 3, 'just': 1}
    output = task_func(input_string)
    assert output == expected_output

def test_task_func_with_empty_string():
    input_string = ""
    expected_output = {}
    output = task_func(input_string)
    assert output == expected_output

def test_task_func_with_one_word_per_line():
    input_string = "word1\nword2\nword3"
    expected_output = {'word1': 1, 'word2': 1, 'word3': 1}
    output = task_func(input_string)
    assert output == expected_output

def test_task_func_with_multiple_occurrences_of_the_same_word():
    input_string = "hello\nworld\nhello\nworld\nhello"
    expected_output = {'hello': 3, 'world': 2}
    output = task_func(input_string)
    assert output == expected_output