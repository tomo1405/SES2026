python
import random
import re
import pytest

from src_0955 import task_func

def test_task_func_valid_inputs():
    target_words = ["apple", "banana", "cherry"]
    n_sentences = 10
    vocabulary = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "peach", "quince", "raspberry", "strawberry", "tangerine", "watermelon"]
    expected_output = ["apple_banana_cherry_date_elderberry_fig_grape_honeydew_kiwi_lemon_mango_nectarine_orange_peach_quince_raspberry_strawberry_tangerine_watermelon",
                       "banana_cherry_date_elderberry_fig_grape_honeydew_kiwi_lemon_mango_nectarine_orange_peach_quince_raspberry_strawberry_tangerine_watermelon",
                       "cherry_date_elderberry_fig_grape_honeydew_kiwi_lemon_mango_nectarine_orange_peach_quince_raspberry_strawberry_tangerine_watermelon",
                       "date_elderberry_fig_grape_honeydew_kiwi_lemon_mango_nectarine_orange_peach_quince_raspberry_strawberry_tangerine_watermelon",
                       "elderberry_fig_grape_honeydew_kiwi_lemon_mango_nectarine_orange_peach_quince_raspberry_strawberry_tangerine_watermelon",
                       "fig_grape_honeydew_kiwi_lemon_mango_nectarine_orange_peach_quince_raspberry_strawberry_tangerine_watermelon",
                       "grape_honeydew_kiwi_lemon_mango_nectarine_orange_peach_quince_raspberry_strawberry_tangerine_watermelon",
                       "honeydew_kiwi_lemon_mango_nectarine_orange_peach_quince_raspberry_strawberry_tangerine_watermelon",
                       "kiwi_lemon_mango_nectarine_orange_peach_quince_raspberry_strawberry_tangerine_watermelon",
                       "lemon_mango_nectarine_orange_peach_quince_raspberry_strawberry_tangerine_watermelon"]

    output = task_func(target_words, n_sentences, vocabulary)

    assert output == expected_output

def test_task_func_invalid_n_sentences():
    target_words = ["apple", "banana", "cherry"]
    n_sentences = -10
    vocabulary = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "peach", "quince", "raspberry", "strawberry", "tangerine", "watermelon"]

    with pytest.raises(ValueError):
        task_func(target_words, n_sentences, vocabulary)

def test_task_func_invalid_vocabulary():
    target_words = ["apple", "banana", "cherry"]
    n_sentences = 10
    vocabulary = []

    with pytest.raises(ValueError):
        task_func(target_words, n_sentences, vocabulary)