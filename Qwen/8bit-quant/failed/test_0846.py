import pytest
from src_0846 import task_func
from Levenshtein import ratio

def test_task_func_identical_texts():
    text1 = "Hello world"
    text2 = "Hello world"
    expected_cosine = 1.0
    expected_levenshtein = 1.0
    assert task_func(text1, text2) == (expected_cosine, expected_levenshtein)

def test_task_func_empty_texts():
    text1 = ""
    text2 = ""
    expected_cosine = 0.0
    expected_levenshtein = 1.0
    assert task_func(text1, text2) == (expected_cosine, expected_levenshtein)

def test_task_func_no_common_words():
    text1 = "Python programming"
    text2 = "Java development"
    expected_cosine = 0.0
    expected_levenshtein = 0.0
    assert task_func(text1, text2) == (expected_cosine, expected_levenshtein)

def test_task_func_one_empty_text():
    text1 = "Hello world"
    text2 = ""
    expected_cosine = 0.0
    expected_levenshtein = 0.0
    assert task_func(text1, text2) == (expected_cosine, expected_levenshtein)

def test_task_func_punctuation():
    text1 = "Hello, world!"
    text2 = "hello world"
    expected_cosine = 1.0
    expected_levenshtein = 1.0
    assert task_func(text1, text2) == (expected_cosine, expected_levenshtein)

def test_task_func_case_insensitivity():
    text1 = "HELLO WORLD"
    text2 = "hello world"
    expected_cosine = 1.0
    expected_levenshtein = 1.0
    assert task_func(text1, text2) == (expected_cosine, expected_levenshtein)

def test_task_func_partial_overlap():
    text1 = "Python is great"
    text2 = "I love Python"
    expected_cosine = 0.5
    expected_levenshtein = 0.5
    assert np.isclose(task_func(text1, text2)[0], expected_cosine)
    assert np.isclose(task_func(text1, text2)[1], expected_levenshtein)