from typing import Counter

from src_0807 import task_func


def test_task_func():
    text = "This is a test sentence. It contains some words and some punctuation."
    n = 2
    expected_output = Counter([('this', 'is'), ('is', 'a'), ('a', 'test'), ('test', 'sentence'), ('sentence', 'contains'), ('contains', 'some'), ('some', 'words'), ('words', 'and'), ('and', 'some'), ('some', 'punctuation')])
    actual_output = task_func(text, n)
    assert actual_output == expected_output, "Output does not match expected output"

def test_task_func_with_different_text():
    text = "Here is another test sentence with some different words."
    n = 3
    expected_output = Counter([('here', 'is', 'another'), ('is', 'another', 'test'), ('another', 'test', 'sentence'), ('test', 'sentence', 'with'), ('sentence', 'with', 'some'), ('with', 'some', 'different'), ('some', 'different', 'words')])
    actual_output = task_func(text, n)
    assert actual_output == expected_output, "Output does not match expected output"

def test_task_func_with_different_n():
    text = "This is a test sentence."
    n = 3
    expected_output = Counter([('this', 'is', 'a'), ('is', 'a', 'test'), ('a', 'test', 'sentence')])
    actual_output = task_func(text, n)
    assert actual_output == expected_output, "Output does not match expected output"

def test_task_func_with_empty_text():
    text = ""
    n = 2
    expected_output = Counter()
    actual_output = task_func(text, n)
    assert actual_output == expected_output, "Output does not match expected output"