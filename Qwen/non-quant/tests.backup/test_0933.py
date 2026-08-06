import pytest
from src_0933 import task_func

def test_task_func_empty_string():
    assert task_func("") == []

def test_task_func_single_character():
    assert task_func("a") == []

def test_task_func_two_characters():
    assert task_func("ab") == [('ab', 1)]

def test_task_func_no_pairs():
    assert task_func("abc") == [('ab', 1), ('bc', 1)]

def test_task_func_with_punctuation():
    assert task_func("Hello, World!") == [('he', 1), ('el', 1), ('ll', 1), ('lo', 1), ('ow', 1), ('wo', 1), ('or', 1), ('rl', 1), ('ld', 1)]

def test_task_func_with_repeated_pairs():
    assert task_func("ababab") == [('ab', 3)]

def test_task_func_case_insensitivity():
    assert task_func("AaBbCc") == [('aa', 1), ('ab', 1), ('bb', 1), ('bc', 1), ('cc', 1)]

def test_task_func_long_string():
    assert task_func("This is a simple test string.") == [('th', 1), ('hi', 1), ('is', 2), ('si', 1), ('im', 1), ('mp', 1), ('pl', 1), ('le', 1), ('te', 1), ('es', 1), ('st', 2), ('tr', 1), ('ri', 1), ('in', 1), ('ng', 1)]