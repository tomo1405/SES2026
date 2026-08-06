import pytest
from src_0960 import task_func

def test_task_func_returns_string():
    text = "Hello World"
    result = task_func(text)
    assert isinstance(result, str)

def test_task_func_returns_random_string():
    text = "Hello World"
    result1 = task_func(text)
    result2 = task_func(text)
    assert result1 != result2

def test_task_func_returns_string_with_random_characters():
    text = "Hello World"
    result = task_func(text)
    assert all(c in string.ascii_lowercase + string.ascii_uppercase for c in result)

def test_task_func_returns_string_with_same_length_as_input():
    text = "Hello World"
    result = task_func(text)
    assert len(result) == len(text)

def test_task_func_returns_string_with_random_characters_in_uppercase():
    text = "Hello World"
    result = task_func(text)
    assert all(c.isupper() for c in result if c.isalpha())

def test_task_func_returns_string_with_random_characters_in_lowercase():
    text = "Hello World"
    result = task_func(text)
    assert all(c.islower() for c in result if c.isalpha())

def test_task_func_returns_string_with_random_characters_in_mixed_case():
    text = "Hello World"
    result = task_func(text)
    assert all(c.isalpha() for c in result)
    assert any(c.isupper() for c in result)
    assert any(c.islower() for c in result)

def test_task_func_returns_string_with_random_characters_in_mixed_case_and_uppercase():
    text = "Hello World"
    result = task_func(text)
    assert all(c.isalpha() for c in result)
    assert any(c.isupper() for c in result)
    assert any(c.islower() for c in result)

def test_task_func_returns_string_with_random_characters_in_mixed_case_and_lowercase():
    text = "Hello World"
    result = task_func(text)
    assert all(c.isalpha() for c in result)
    assert any(c.isupper() for c in result)
    assert any(c.islower() for c in result)

def test_task_func_returns_string_with_random_characters_in_mixed_case_and_uppercase_and_lowercase():
    text = "Hello World"
    result = task_func(text)
    assert all(c.isalpha() for c in result)
    assert any(c.isupper() for c in result)
    assert any(c.islower() for c in result)