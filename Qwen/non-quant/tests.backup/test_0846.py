import pytest
from src_0846 import task_func
import numpy as np
from collections import Counter
from Levenshtein import ratio

def test_task_func_identical_texts():
    text1 = "Hello world"
    text2 = "Hello world"
    expected_cosine_similarity = 1.0
    expected_levenshtein_ratio = 1.0
    result = task_func(text1, text2)
    assert np.isclose(result[0], expected_cosine_similarity)
    assert np.isclose(result[1], expected_levenshtein_ratio)

def test_task_func_different_texts():
    text1 = "Hello world"
    text2 = "Hi there"
    expected_cosine_similarity = 0.5
    expected_levenshtein_ratio = 0.5
    result = task_func(text1, text2)
    assert np.isclose(result[0], expected_cosine_similarity)
    assert np.isclose(result[1], expected_levenshtein_ratio)

def test_task_func_empty_texts():
    text1 = ""
    text2 = ""
    expected_cosine_similarity = 0.0
    expected_levenshtein_ratio = 1.0
    result = task_func(text1, text2)
    assert np.isclose(result[0], expected_cosine_similarity)
    assert np.isclose(result[1], expected_levenshtein_ratio)

def test_task_func_one_empty_text():
    text1 = ""
    text2 = "Hello world"
    expected_cosine_similarity = 0.0
    expected_levenshtein_ratio = 0.0
    result = task_func(text1, text2)
    assert np.isclose(result[0], expected_cosine_similarity)
    assert np.isclose(result[1], expected_levenshtein_ratio)

def test_task_func_special_characters():
    text1 = "Hello, world!"
    text2 = "hello world"
    expected_cosine_similarity = 1.0
    expected_levenshtein_ratio = 1.0
    result = task_func(text1, text2)
    assert np.isclose(result[0], expected_cosine_similarity)
    assert np.isclose(result[1], expected_levenshtein_ratio)

def test_task_func_case_insensitivity():
    text1 = "HELLO WORLD"
    text2 = "hello world"
    expected_cosine_similarity = 1.0
    expected_levenshtein_ratio = 1.0
    result = task_func(text1, text2)
    assert np.isclose(result[0], expected_cosine_similarity)
    assert np.isclose(result[1], expected_levenshtein_ratio)