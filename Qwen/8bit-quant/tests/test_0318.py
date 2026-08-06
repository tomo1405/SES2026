import pytest
from src_0318 import task_func

def test_task_func_empty_string():
    result = task_func("")
    assert result == {}

def test_task_func_string_with_only_brackets():
    result = task_func("[]")
    assert result == {}

def test_task_func_string_with_text_and_brackets():
    result = task_func("This is a test [with brackets]")
    assert "test" in result
    assert "brackets" not in result

def test_task_func_string_with_multiple_brackets():
    result = task_func("This is a test [with] multiple [brackets]")
    assert "test" in result
    assert "multiple" in result
    assert "brackets" not in result

def test_task_func_string_with_special_characters():
    result = task_func("This is a test! @# $%^&*()")
    assert "test" in result
    assert "!" not in result
    assert "@" not in result

def test_task_func_string_with_numbers():
    result = task_func("This is a test with numbers 12345")
    assert "test" in result
    assert "numbers" in result
    assert "12345" not in result

def test_task_func_string_with_whitespace():
    result = task_func("   This is a test with whitespace   ")
    assert "test" in result
    assert "whitespace" in result

def test_task_func_string_with_punctuation():
    result = task_func("This is a test, with punctuation.")
    assert "test" in result
    assert "punctuation" in result
    assert "," not in result
    assert "." not in result

def test_task_func_string_with_apostrophes():
    result = task_func("It's a test with apostrophes")
    assert "test" in result
    assert "apostrophes" in result
    assert "It's" in result

def test_task_func_string_with_quotes():
    result = task_func('This is a "test" with quotes')
    assert "test" in result
    assert "quotes" in result
    assert '"' not in result

def test_task_func_string_with_hyphens():
    result = task_func("This is a test-with-hyphens")
    assert "test" in result
    assert "hyphens" in result
    assert "-" not in result