import pytest
from src_0957 import task_func

def test_task_func_no_punctuation():
    input_text = "Hello, World!"
    expected_output = "Hello World"
    assert task_func(input_text) == expected_output

def test_task_func_replacements():
    input_text = "Hello\tWorld\nTest"
    expected_output = "Hello__World___Test"
    assert task_func(input_text) == expected_output

def test_task_func_random_case():
    input_text = "hello"
    output1 = task_func(input_text, seed=0)
    output2 = task_func(input_text, seed=0)
    assert output1 == output2
    assert output1 != input_text

def test_task_func_empty_string():
    input_text = ""
    expected_output = ""
    assert task_func(input_text) == expected_output

def test_task_func_whitespace():
    input_text = "   \t\n"
    expected_output = "____"
    assert task_func(input_text) == expected_output

def test_task_func_special_characters():
    input_text = "!@#$%^&*()_+"
    expected_output = ""
    assert task_func(input_text) == expected_output

def test_task_func_mixed_content():
    input_text = "Hello, World! 123"
    expected_output = "Hello_World_123"
    assert task_func(input_text) == expected_output