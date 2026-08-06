python
import random
import re
import pytest

from src_0955 import task_func

def test_task_func():
    # Test case 1: target_words is a list of strings, n_sentences is a positive integer, vocabulary is a non-empty list of strings
    target_words = ["apple", "banana", "cherry"]
    n_sentences = 5
    vocabulary = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "peach", "quince", "raspberry", "strawberry", "tangerine", "watermelon"]
    expected_result = ["apple_banana_cherry_date_elderberry_fig_grape_honeydew_kiwi_lemon_mango_nectarine_orange_peach_quince_raspberry_strawberry_tangerine_watermelon", "apple_banana_cherry_date_elderberry_fig_grape_honeydew_kiwi_lemon_mango_nectarine_orange_peach_quince_raspberry_strawberry_tangerine_watermelon", "apple_banana_cherry_date_elderberry_fig_grape_honeydew_kiwi_lemon_mango_nectarine_orange_peach_quince_raspberry_strawberry_tangerine_watermelon", "apple_banana_cherry_date_elderberry_fig_grape_honeydew_kiwi_lemon_mango_nectarine_orange_peach_quince_raspberry_strawberry_tangerine_watermelon", "apple_banana_cherry_date_elderberry_fig_grape_honeydew_kiwi_lemon_mango_nectarine_orange_peach_quince_raspberry_strawberry_tangerine_watermelon"]
    assert task_func(target_words, n_sentences, vocabulary) == expected_result

    # Test case 2: target_words is a list of strings, n_sentences is a negative integer, vocabulary is a non-empty list of strings
    target_words = ["apple", "banana", "cherry"]
    n_sentences = -5
    vocabulary = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "peach", "quince", "raspberry", "strawberry", "tangerine", "watermelon"]
    with pytest.raises(ValueError):
        task_func(target_words, n_sentences, vocabulary)

    # Test case 3: target_words is a list of strings, n_sentences is a positive integer, vocabulary is an empty list of strings
    target_words = ["apple", "banana", "cherry"]
    n_sentences = 5
    vocabulary = []
    with pytest.raises(ValueError):
        task_func(target_words, n_sentences, vocabulary)

    # Test case 4: target_words is a list of strings, n_sentences is a positive integer, vocabulary is a list of strings with duplicates
    target_words = ["apple", "banana", "cherry"]
    n_sentences = 5
    vocabulary = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "peach", "quince", "raspberry", "strawberry", "tangerine", "watermelon", "apple", "banana", "cherry"]
    expected_result = ["apple_banana_cherry_date_elderberry_fig_grape_honeydew_kiwi_lemon_mango_nectarine_orange_peach_quince_raspberry_strawberry_tangerine_watermelon", "apple_banana_cherry_date_elderberry_fig_grape_honeydew_kiwi_lemon_mango_nectarine_orange_peach_quince_raspberry_strawberry_tangerine_watermelon", "apple_banana_cherry_date_elderberry_fig_grape_honeydew_kiwi_lemon_mango_nectarine_orange_peach_quince_raspberry_strawberry_tangerine_watermelon", "apple_banana_cherry_date_elderberry_fig_grape_honeydew_kiwi_lemon_mango_nectarine_orange_peach_quince_raspberry_strawberry_tangerine_watermelon", "apple_banana_cherry_date_elderberry_fig_grape_honeydew_kiwi_lemon_mango_nectarine_orange_peach_quince_raspberry_strawberry_tangerine_watermelon"]
    assert task_func(target_words, n_sentences, vocabulary) == expected_result

    # Test case 5: target_words is a list of strings, n_sentences is a positive integer, vocabulary is a list of strings with non-alphabetic characters
    target_words = ["apple", "banana", "cherry"]
    n_sentences = 5
    vocabulary = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "peach", "quince", "raspberry", "strawberry", "tangerine", "watermelon", "123", "abc", "xyz"]
    expected_result = ["apple_banana_cherry_date_elderberry_fig_grape_honeydew_kiwi_lemon_mango_nectarine_orange_peach_quince_raspberry_strawberry_tangerine_watermelon", "apple_banana_cherry_date_elderberry_fig_grape_honeydew_kiwi_lemon_mango_nectarine_orange_peach_quince_raspberry_strawberry_tangerine_watermelon", "apple_banana_cherry_date_elderberry_fig_grape_honeydew_kiwi_lemon_mango_nectarine_orange_peach_quince_raspberry_strawberry_tangerine_watermelon", "apple_banana_cherry_date_elderberry_fig_grape_honeydew_kiwi_lemon_mango_nectarine_orange_peach_quince_raspberry_strawberry_tangerine_watermelon", "apple_banana_cherry_date_elderberry_fig_grape_honeydew_kiwi_lemon_mango_nectarine_orange_peach_quince_raspberry_strawberry_tangerine_watermelon"]
    assert task_func(target_words, n_sentences, vocabulary) == expected_result