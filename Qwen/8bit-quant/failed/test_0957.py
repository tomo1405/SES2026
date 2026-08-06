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
    # Since the output is random, we can only check that it has the same length and contains the same characters
    output = task_func(input_text)
    assert len(output) == len(input_text)
    assert set(output.lower()) == set(input_text)

def test_task_func_with_seed():
    input_text = "hello"
    seed = 42
    output1 = task_func(input_text, seed=seed)
    output2 = task_func(input_text, seed=seed)
    assert output1 == output2

def test_task_func_empty_string():
    input_text = ""
    expected_output = ""
    assert task_func(input_text) == expected_output

def test_task_func_only_punctuation():
    input_text = "!@#$%^&*()"
    expected_output = ""
    assert task_func(input_text) == expected_output