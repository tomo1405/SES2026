import pytest
from src_0850 import task_func
from collections import Counter

def test_task_func_with_empty_string():
    assert task_func("") == {}

def test_task_func_with_single_word():
    assert task_func("hello") == {}

def test_task_func_with_single_non_stopword():
    assert task_func("world") == {'world': 1}

def test_task_func_with_multiple_lines():
    input_string = "hello world\nthis is a test"
    expected_output = {'world': 1, 'test': 1}
    assert task_func(input_string) == expected_output

def test_task_func_with_punctuation():
    input_string = "hello, world! this is a test."
    expected_output = {'hello': 1, 'world': 1, 'test': 1}
    assert task_func(input_string) == expected_output

def test_task_func_with_stopwords_only():
    input_string = "this is a test of the system"
    expected_output = {}
    assert task_func(input_string) == expected_output

def test_task_func_with_mixed_case():
    input_string = "Hello World\nHELLO world"
    expected_output = {'hello': 2, 'world': 2}
    assert task_func(input_string) == expected_output

def test_task_func_with_numbers():
    input_string = "hello world 1234"
    expected_output = {'hello': 1, 'world': 1}
    assert task_func(input_string) == expected_output

def test_task_func_with_special_characters():
    input_string = "hello @world #test"
    expected_output = {'hello': 1, 'world': 1, 'test': 1}
    assert task_func(input_string) == expected_output