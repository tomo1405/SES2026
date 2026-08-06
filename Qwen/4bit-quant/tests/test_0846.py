import pytest
from src_0846 import task_func

def test_task_func_identical_texts():
    text1 = "Hello, world!"
    text2 = "Hello, world!"
    expected_cosine = 1.0
    expected_levenshtein = 1.0
    result = task_func(text1, text2)
    assert result == (expected_cosine, expected_levenshtein)

def test_task_func_different_texts():
    text1 = "Python is great"
    text2 = "Python rocks"
    expected_cosine = pytest.approx(0.5, abs=0.1)  # Approximate value due to nature of cosine similarity
    expected_levenshtein = pytest.approx(0.75, abs=0.1)  # Approximate value due to nature of Levenshtein ratio
    result = task_func(text1, text2)
    assert result[0] == expected_cosine
    assert result[1] == expected_levenshtein

def test_task_func_empty_texts():
    text1 = ""
    text2 = ""
    expected_cosine = 0.0
    expected_levenshtein = 1.0
    result = task_func(text1, text2)
    assert result == (expected_cosine, expected_levenshtein)

def test_task_func_one_empty_text():
    text1 = "Some text"
    text2 = ""
    expected_cosine = 0.0
    expected_levenshtein = 0.0
    result = task_func(text1, text2)
    assert result == (expected_cosine, expected_levenshtein)

def test_task_func_no_common_words():
    text1 = "Python"
    text2 = "Java"
    expected_cosine = 0.0
    expected_levenshtein = pytest.approx(0.0, abs=0.1)  # Approximate value due to nature of Levenshtein ratio
    result = task_func(text1, text2)
    assert result == (expected_cosine, expected_levenshtein)

def test_task_func_special_characters():
    text1 = "Hello, World!"
    text2 = "Hello World"
    expected_cosine = 1.0
    expected_levenshtein = 1.0
    result = task_func(text1, text2)
    assert result == (expected_cosine, expected_levenshtein)

def test_task_func_case_insensitivity():
    text1 = "Python is great"
    text2 = "pYTHON IS gREAT"
    expected_cosine = 1.0
    expected_levenshtein = 1.0
    result = task_func(text1, text2)
    assert result == (expected_cosine, expected_levenshtein)