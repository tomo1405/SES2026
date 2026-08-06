import pytest
from src_1127 import task_func

def test_task_func_with_alphanumeric_input():
    input_str = "HelloWorld123"
    expected_output = "a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e"
    assert task_func(input_str) == expected_output

def test_task_func_with_special_characters():
    input_str = "Hello!@#World$%^&*()"
    expected_output = "a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e"
    assert task_func(input_str) == expected_output

def test_task_func_with_whitespace():
    input_str = "Hello World 123"
    expected_output = "a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e"
    assert task_func(input_str) == expected_output

def test_task_func_with_empty_string():
    input_str = ""
    expected_output = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    assert task_func(input_str) == expected_output

def test_task_func_with_only_special_characters():
    input_str = "!@#$%^&*()"
    expected_output = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    assert task_func(input_str) == expected_output