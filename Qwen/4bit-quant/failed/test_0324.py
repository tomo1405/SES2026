import pytest
from src_0324 import task_func
import numpy as np

def test_task_func_with_default_parameters():
    text = "apple [banana] orange apple banana"
    expected_word_freqs = {'apple': 2, 'banana': 2, 'orange': 1}
    result_word_freqs, _ = task_func(text)
    assert result_word_freqs == expected_word_freqs

def test_task_func_with_custom_num_gaussians():
    text = "apple [banana] orange apple banana"
    num_gaussians = 2
    _, means = task_func(text, num_gaussians=num_gaussians)
    assert len(means) == num_gaussians

def test_task_func_with_zero_gaussians():
    text = "apple [banana] orange apple banana"
    with pytest.raises(ValueError, match='Number of Gaussians must be greater than 0.'):
        task_func(text, num_gaussians=0)

def test_task_func_with_more_gaussians_than_unique_words():
    text = "apple [banana] orange"
    num_gaussians = 5
    with pytest.raises(Exception, match='Number of Gaussians must be less than or equal to the number of unique words.'):
        task_func(text, num_gaussians=num_gaussians)

def test_task_func_with_different_seed():
    text = "apple [banana] orange apple banana"
    _, means_1 = task_func(text, seed=1)
    _, means_2 = task_func(text, seed=2)
    assert not np.array_equal(means_1, means_2)

def test_task_func_with_no_brackets():
    text = "apple banana orange"
    expected_word_freqs = {'apple': 1, 'banana': 1, 'orange': 1}
    result_word_freqs, _ = task_func(text)
    assert result_word_freqs == expected_word_freqs

def test_task_func_with_empty_text():
    text = ""
    expected_word_freqs = {}
    result_word_freqs, _ = task_func(text)
    assert result_word_freqs == expected_word_freqs