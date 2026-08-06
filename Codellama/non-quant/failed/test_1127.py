import pytest
from src_1127 import task_func

def test_task_func():
    input_str = "Hello World!"
    expected_output = "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
    assert task_func(input_str) == expected_output

def test_task_func_with_empty_string():
    input_str = ""
    expected_output = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    assert task_func(input_str) == expected_output

def test_task_func_with_special_chars():
    input_str = "Hello World!@#$%^&*()_+-=[]{}|;':\"<>,./?"
    expected_output = "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
    assert task_func(input_str) == expected_output

def test_task_func_with_unicode_chars():
    input_str = "Hello World! 😊"
    expected_output = "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
    assert task_func(input_str) == expected_output