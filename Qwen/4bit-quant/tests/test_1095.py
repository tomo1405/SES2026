import pytest
from src_1095 import task_func

def test_task_func_with_no_dollar_words():
    text = "This is a test without any dollar words."
    assert task_func(text) == []

def test_task_func_with_single_dollar_word():
    text = "$example"
    assert task_func(text) == [("example", 1)]

def test_task_func_with_multiple_dollar_words():
    text = "$example $example $test $test $test $another"
    assert task_func(text) == [("test", 3), ("example", 2), ("another", 1)]

def test_task_func_with_mixed_case():
    text = "$Example $example $EXAMPLE"
    assert task_func(text) == [("example", 3)]

def test_task_func_with_special_characters():
    text = "$$special $$characters $special $characters"
    assert task_func(text) == [("special", 2), ("characters", 2)]

def test_task_func_with_empty_string():
    text = ""
    assert task_func(text) == []

def test_task_func_with_only_dollar_signs():
    text = "$$$$$$$"
    assert task_func(text) == []