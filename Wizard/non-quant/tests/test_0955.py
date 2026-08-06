python
import random
import re
import pytest

from src_0955 import task_func

def test_task_func():
    # Test case 1: target_words is a list of strings, n_sentences is a positive integer, vocabulary is a list of strings
    target_words = ["apple", "banana", "cherry"]
    n_sentences = 5
    vocabulary = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
    expected_result = ["apple_banana_cherry_date_elderberry_fig_grape_honeydew_kiwi_lemon",
                       "apple_banana_cherry_date_elderberry_fig_grape_honeydew_kiwi_lemon",
                       "apple_banana_cherry_date_elderberry_fig_grape_honeydew_kiwi_lemon",
                       "apple_banana_cherry_date_elderberry_fig_grape_honeydew_kiwi_lemon",
                       "apple_banana_cherry_date_elderberry_fig_grape_honeydew_kiwi_lemon"]
    assert task_func(target_words, n_sentences, vocabulary) == expected_result

    # Test case 2: target_words is a list of strings, n_sentences is a negative integer, vocabulary is a list of strings
    target_words = ["apple", "banana", "cherry"]
    n_sentences = -5
    vocabulary = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
    with pytest.raises(ValueError):
        task_func(target_words, n_sentences, vocabulary)

    # Test case 3: target_words is a list of strings, n_sentences is a positive integer, vocabulary is an empty list
    target_words = ["apple", "banana", "cherry"]
    n_sentences = 5
    vocabulary = []
    with pytest.raises(ValueError):
        task_func(target_words, n_sentences, vocabulary)

    # Test case 4: target_words is a list of strings, n_sentences is a positive integer, vocabulary is a list of strings with duplicates
    target_words = ["apple", "banana", "cherry"]
    n_sentences = 5
    vocabulary = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "apple"]
    expected_result = ["apple_banana_cherry_date_elderberry_fig_grape_honeydew_kiwi_lemon",
                       "apple_banana_cherry_date_elderberry_fig_grape_honeydew_kiwi_lemon",
                       "apple_banana_cherry_date_elderberry_fig_grape_honeydew_kiwi_lemon",
                       "apple_banana_cherry_date_elderberry_fig_grape_honeydew_kiwi_lemon",
                       "apple_banana_cherry_date_elderberry_fig_grape_honeydew_kiwi_lemon"]
    assert task_func(target_words, n_sentences, vocabulary) == expected_result

    # Test case 5: target_words is a list of strings, n_sentences is a positive integer, vocabulary is a list of strings with non-alphanumeric characters
    target_words = ["apple", "banana", "cherry"]
    n_sentences = 5
    vocabulary = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "apple!"]
    expected_result = ["apple_banana_cherry_date_elderberry_fig_grape_honeydew_kiwi_lemon",
                       "apple_banana_cherry_date_elderberry_fig_grape_honeydew_kiwi_lemon",
                       "apple_banana_cherry_date_elderberry_fig_grape_honeydew_kiwi_lemon",
                       "apple_banana_cherry_date_elderberry_fig_grape_honeydew_kiwi_lemon",
                       "apple_banana_cherry_date_elderberry_fig_grape_honeydew_kiwi_lemon"]
    assert task_func(target_words, n_sentences, vocabulary) == expected_result

    # Test case 6: target_words is a list of strings, n_sentences is a positive integer, vocabulary is a list of strings with non-alphanumeric characters and duplicates
    target_words = ["apple", "banana", "cherry"]
    n_sentences = 5
    vocabulary = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "apple!", "apple"]
    expected_result = ["apple_banana_cherry_date_elderberry_fig_grape_honeydew_kiwi_lemon",
                       "apple_banana_cherry_date_elderberry_fig_grape_honeydew_kiwi_lemon",
                       "apple_banana_cherry_date_elderberry_fig_grape_honeydew_kiwi_lemon",
                       "apple_banana_cherry_date_elderberry_fig_grape_honeydew_kiwi_lemon",
                       "apple_banana_cherry_date_elderberry_fig_grape_honeydew_kiwi_lemon"]
    assert task_func(target_words, n_sentences, vocabulary) == expected_result