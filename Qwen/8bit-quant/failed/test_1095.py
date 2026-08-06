import pytest
from src_1095 import task_func
from nltk.tokenize import RegexpTokenizer
from collections import Counter

def test_task_func_no_dollar_words():
    text = "This is a test text without any dollar words."
    expected_output = []
    assert task_func(text) == expected_output

def test_task_func_single_dollar_word():
    text = "This is a test with one $$word."
    expected_output = [('word', 1)]
    assert task_func(text) == expected_output

def test_task_func_multiple_dollar_words():
    text = "This is a test with multiple $$words and $$words."
    expected_output = [('words', 2)]
    assert task_func(text) == expected_output

def test_task_func_mixed_case():
    text = "This is a test with mixed $$Words and $$words."
    expected_output = [('words', 2), ('Words', 1)]
    assert task_func(text) == expected_output

def test_task_func_top_five():
    text = "This is a test with five $$one, four $$two, three $$three, two $$four, and one $$five."
    expected_output = [('one', 1), ('two', 1), ('three', 1), ('four', 1), ('five', 1)]
    assert task_func(text) == expected_output

def test_task_func_empty_string():
    text = ""
    expected_output = []
    assert task_func(text) == expected_output

def test_task_func_only_dollar_signs():
    text = "$$$"
    expected_output = []
    assert task_func(text) == expected_output

def test_task_func_special_characters():
    text = "This is a test with special characters $$@# and $$%^&*."
    expected_output = []
    assert task_func(text) == expected_output