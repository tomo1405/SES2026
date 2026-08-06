import pytest
from src_0933 import task_func

def test_task_func_with_empty_string():
    assert task_func("") == []

def test_task_func_with_single_character():
    assert task_func("a") == []

def test_task_func_with_no_pairs():
    assert task_func("ab") == [('ab', 1)]

def test_task_func_with_one_pair():
    assert task_func("abc") == [('ab', 1)]

def test_task_func_with_multiple_pairs():
    assert task_func("aabbcc") == [('aa', 2)]

def test_task_func_with_mixed_case():
    assert task_func("AaBbCc") == [('aa', 1)]

def test_task_func_with_non_alphabetic_characters():
    assert task_func("a!b@c#") == [('ab', 1)]

def test_task_func_with_repeated_pairs():
    assert task_func("ababab") == [('ab', 3)]

def test_task_func_with_unique_pairs():
    assert task_func("abcdefg") == [('ab', 1)]

def test_task_func_with_tie_in_most_common():
    assert task_func("aabbaa") == [('aa', 3)]