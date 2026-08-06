import pytest
from src_0957 import task_func

def test_task_func_no_punctuation_no_seed():
    input_text = "Hello, World!"
    expected_output = "HeLlO__WoRlD"
    assert task_func(input_text) == expected_output

def test_task_func_with_punctuation_with_seed():
    input_text = "Hello, World! \t\n"
    seed_value = 42
    expected_output = "HeLlO__WoRlD___"
    assert task_func(input_text, seed=seed_value) == expected_output

def test_task_func_empty_string():
    input_text = ""
    expected_output = ""
    assert task_func(input_text) == expected_output

def test_task_func_only_spaces():
    input_text = "   "
    expected_output = "___"
    assert task_func(input_text) == expected_output

def test_task_func_only_tabs_and_newlines():
    input_text = "\t\n\t"
    expected_output = "______"
    assert task_func(input_text) == expected_output

def test_task_func_mixed_characters():
    input_text = "a1b!c@d#e$f%g^h&i*j(k)"
    expected_output = "A1BcAdEfGhIjK"
    assert task_func(input_text) == expected_output

def test_task_func_case_insensitivity():
    input_text = "hello world"
    seed_value = 0
    expected_output = "hElLo_wOrLd"
    assert task_func(input_text, seed=seed_value) == expected_output

def test_task_func_randomness():
    input_text = "random"
    seed_value = 123
    expected_output = "RaNdOm"
    assert task_func(input_text, seed=seed_value) == expected_output