import pytest
from src_1095 import task_func

def test_task_func():
    text = "Hello, world! This is a test sentence."
    expected_result = [('world', 1), ('test', 1), ('sentence', 1), ('hello', 1), ('is', 1)]
    assert task_func(text) == expected_result

def test_task_func_with_empty_string():
    text = ""
    expected_result = []
    assert task_func(text) == expected_result

def test_task_func_with_single_word():
    text = "hello"
    expected_result = [('hello', 1)]
    assert task_func(text) == expected_result

def test_task_func_with_multiple_words():
    text = "hello world"
    expected_result = [('hello', 1), ('world', 1)]
    assert task_func(text) == expected_result

def test_task_func_with_duplicate_words():
    text = "hello hello"
    expected_result = [('hello', 2)]
    assert task_func(text) == expected_result

def test_task_func_with_dollar_prefixed_words():
    text = "$hello $world"
    expected_result = [('hello', 1), ('world', 1)]
    assert task_func(text) == expected_result

def test_task_func_with_dollar_prefixed_words_and_duplicates():
    text = "$hello $hello"
    expected_result = [('hello', 2)]
    assert task_func(text) == expected_result