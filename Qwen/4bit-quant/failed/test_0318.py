import pytest
from src_0318 import task_func

def test_task_func_empty_string():
    result = task_func("")
    assert result == {}

def test_task_func_string_with_only_brackets():
    result = task_func("[]")
    assert result == {}

def test_task_func_string_with_no_words():
    result = task_func("[ ]")
    assert result == {}

def test_task_func_string_with_text():
    result = task_func("This is a test string.")
    assert isinstance(result, dict)
    assert "test" in result
    assert "string" in result
    assert "is" in result
    assert "a" in result

def test_task_func_string_with_brackets():
    result = task_func("This [is] a test string.")
    assert isinstance(result, dict)
    assert "test" in result
    assert "string" in result
    assert "is" in result
    assert "a" in result

def test_task_func_string_with_special_characters():
    result = task_func("This is a test! @# string.")
    assert isinstance(result, dict)
    assert "test" in result
    assert "string" in result
    assert "is" in result
    assert "a" in result

def test_task_func_string_with_numbers():
    result = task_func("This is a test 123 string.")
    assert isinstance(result, dict)
    assert "test" in result
    assert "string" in result
    assert "is" in result
    assert "a" in result
    assert "123" not in result

def test_task_func_string_with_multiple_sentences():
    result = task_func("This is a test. Another sentence here.")
    assert isinstance(result, dict)
    assert "test" in result
    assert "another" in result
    assert "sentence" in result
    assert "here" in result

def test_task_func_string_with_whitespace():
    result = task_func("   This is a test string.   ")
    assert isinstance(result, dict)
    assert "test" in result
    assert "string" in result
    assert "is" in result
    assert "a" in result

def test_task_func_string_with_repeated_words():
    result = task_func("This is a test test string.")
    assert isinstance(result, dict)
    assert "test" in result
    assert "string" in result
    assert "is" in result
    assert "a" in result