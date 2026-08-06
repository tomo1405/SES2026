import pytest
from src_0727 import task_func
import random
from nltk.corpus import words

# Ensure the words corpus is downloaded
import nltk
nltk.download('words')

def test_task_func_no_words():
    assert task_func("123456", 3) == []

def test_task_func_fewer_words_than_n():
    result = task_func("hello world", 5)
    assert len(result) == 2
    assert set(result).issubset({"hello", "world"})

def test_task_func_more_words_than_n():
    result = task_func("hello world this is a test", 3)
    assert len(result) == 3
    assert set(result).issubset({"hello", "world", "this", "is", "a", "test"})

def test_task_func_n_is_zero():
    assert task_func("hello world", 0) == []

def test_task_func_n_is_negative():
    assert task_func("hello world", -1) == []

def test_task_func_all_non_english():
    assert task_func("!@#$%^&*", 3) == []

def test_task_func_random_sampling():
    random.seed(0)  # For reproducibility
    result = task_func("hello world this is a test", 3)
    assert len(result) == 3
    assert set(result).issubset({"hello", "world", "this", "is", "a", "test"})
    # Check that the order is consistent with the random seed
    assert result == ['is', 'test', 'this']

def test_task_func_with_punctuation():
    result = task_func("hello, world!", 2)
    assert len(result) == 2
    assert set(result).issubset({"hello", "world"})

def test_task_func_with_multiple_spaces():
    result = task_func("   hello   world   ", 2)
    assert len(result) == 2
    assert set(result).issubset({"hello", "world"})

def test_task_func_with_mixed_case():
    result = task_func("Hello World", 2)
    assert len(result) == 2
    assert set(result).issubset({"hello", "world"})

def test_task_func_with_large_input():
    large_string = " ".join(words.words()[:1000])
    result = task_func(large_string, 10)
    assert len(result) == 10
    assert all(word in words.words() for word in result)

def test_task_func_with_single_word():
    result = task_func("hello", 1)
    assert len(result) == 1
    assert result[0] == "hello"