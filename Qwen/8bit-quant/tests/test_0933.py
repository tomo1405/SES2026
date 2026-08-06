import pytest
from src_0933 import task_func

def test_task_func_empty_string():
    assert task_func("") == []

def test_task_func_single_character():
    assert task_func("a") == []

def test_task_func_two_characters():
    assert task_func("ab") == [('ab', 1)]

def test_task_func_no_pairs():
    assert task_func("1234!@#$") == []

def test_task_func_simple_case():
    assert task_func("hello") == [('ll', 1)]

def test_task_func_multiple_most_common_pairs():
    assert task_func("aabbcc") == [('aa', 1), ('bb', 1), ('cc', 1)]

def test_task_func_case_insensitivity():
    assert task_func("Hello") == [('ll', 1)]

def test_task_func_punctuation():
    assert task_func("he,llo!") == [('el', 1), ('ll', 1), ('lo', 1)]

def test_task_func_long_string():
    assert task_func("mississippi") == [('is', 2), ('ss', 2), ('si', 2)]