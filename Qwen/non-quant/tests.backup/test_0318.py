import pytest
from src_0318 import task_func
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import re

def test_task_func_empty_string():
    assert task_func("") == {}

def test_task_func_string_with_only_brackets():
    assert task_func("[]") == {}
    assert task_func("[example]") == {}

def test_task_func_string_with_text():
    result = task_func("This is an example string.")
    assert isinstance(result, dict)
    assert "example" in result
    assert "string" in result
    assert "this" in result
    assert "is" in result
    assert "an" in result

def test_task_func_string_with_brackets():
    result = task_func("This [is] an example string.")
    assert isinstance(result, dict)
    assert "example" in result
    assert "string" in result
    assert "this" in result
    assert "is" not in result
    assert "an" in result

def test_task_func_string_with_numbers():
    result = task_func("This is an example string with numbers 123.")
    assert isinstance(result, dict)
    assert "example" in result
    assert "string" in result
    assert "this" in result
    assert "is" in result
    assert "an" in result
    assert "numbers" in result
    assert "123" not in result

def test_task_func_string_with_special_characters():
    result = task_func("This is an example string with special characters!@#")
    assert isinstance(result, dict)
    assert "example" in result
    assert "string" in result
    assert "this" in result
    assert "is" in result
    assert "an" in result
    assert "special" in result
    assert "characters" in result
    assert "!@#" not in result

def test_task_func_string_with_multiple_words():
    result = task_func("This is an example string with multiple words.")
    assert isinstance(result, dict)
    assert "example" in result
    assert "string" in result
    assert "this" in result
    assert "is" in result
    assert "an" in result
    assert "multiple" in result
    assert "words" in result

def test_task_func_string_with_repeated_words():
    result = task_func("This is this is an example string.")
    assert isinstance(result, dict)
    assert "example" in result
    assert "string" in result
    assert "this" in result
    assert "is" in result
    assert "an" in result

def test_task_func_string_with_single_word():
    result = task_func("Example")
    assert isinstance(result, dict)
    assert "example" in result

def test_task_func_string_with_whitespace():
    result = task_func("   This is an example string.   ")
    assert isinstance(result, dict)
    assert "example" in result
    assert "string" in result
    assert "this" in result
    assert "is" in result
    assert "an" in result