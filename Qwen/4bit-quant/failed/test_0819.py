import pytest
from src_0819 import task_func

def test_task_func_with_punctuation():
    text = "Hello, world! This is a test."
    expected_output = ['hello', 'world', 'this', 'is', 'a', 'test']
    assert task_func(text) == expected_output

def test_task_func_with_multiple_spaces():
    text = "   Multiple   spaces   should   be   handled.  "
    expected_output = ['multiple', 'spaces', 'should', 'be', 'handled']
    assert task_func(text) == expected_output

def test_task_func_with_no_punctuation():
    text = "No punctuation here"
    expected_output = ['no', 'punctuation', 'here']
    assert task_func(text) == expected_output

def test_task_func_with_empty_string():
    text = ""
    expected_output = []
    assert task_func(text) == expected_output

def test_task_func_with_only_punctuation():
    text = "!@#$%^&*()"
    expected_output = []
    assert task_func(text) == expected_output

def test_task_func_with_mixed_case():
    text = "MiXeD CaSe TeSt"
    expected_output = ['mixed', 'case', 'test']
    assert task_func(text) == expected_output