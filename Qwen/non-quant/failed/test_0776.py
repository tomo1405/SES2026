import pytest
from src_0776 import task_func

def test_task_func_no_hyphen():
    assert task_func("abc") == {'a': 1, 'b': 1, 'c': 1, **{letter: 0 for letter in 'defghijklmnopqrstuvwxyz'}}

def test_task_func_with_hyphen():
    assert task_func("abc-def") == {'a': 1, 'b': 1, 'c': 1, **{letter: 0 for letter in 'defghijklmnopqrstuvwxyz'}}

def test_task_func_empty_string():
    assert task_func("") == {letter: 0 for letter in 'abcdefghijklmnopqrstuvwxyz'}

def test_task_func_non_alpha_characters():
    assert task_func("abc-123") == {letter: 0 for letter in 'abcdefghijklmnopqrstuvwxyz'}

def test_task_func_single_letter():
    assert task_func("a-b") == {'a': 1, **{letter: 0 for letter in 'bcdefghijklmnopqrstuvwxyz'}}

def test_task_func_all_letters():
    assert task_func("abcdefghijklmnopqrstuvwxyz-a") == {letter: 1 for letter in 'abcdefghijklmnopqrstuvwxyz'}

def test_task_func_repeated_letters():
    assert task_func("aabbcc-a") == {'a': 2, 'b': 2, 'c': 2, **{letter: 0 for letter in 'defghijklmnopqrstuvwxyz'}}