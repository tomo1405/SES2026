import pytest
from src_0324 import task_func
import numpy as np

def test_task_func_basic():
    text = "apple banana apple [fruit] orange banana"
    expected_freqs = {'apple': 2, 'banana': 2, 'orange': 1}
    expected_means_shape = (1, 1)  # Since num_gaussians is 1 by default

    word_freqs, means = task_func(text)

    assert word_freqs == expected_freqs
    assert means.shape == expected_means_shape

def test_task_func_multiple_gaussians():
    text = "apple banana apple [fruit] orange banana"
    num_gaussians = 2
    expected_means_shape = (2, 1)

    word_freqs, means = task_func(text, num_gaussians=num_gaussians)

    assert len(word_freqs) >= num_gaussians
    assert means.shape == expected_means_shape

def test_task_func_zero_gaussians():
    text = "apple banana apple [fruit] orange banana"
    num_gaussians = 0

    with pytest.raises(ValueError, match='Number of Gaussians must be greater than 0.'):
        task_func(text, num_gaussians=num_gaussians)

def test_task_func_more_gaussians_than_unique_words():
    text = "apple banana apple [fruit] orange banana"
    num_gaussians = 5

    with pytest.raises(Exception, match='Number of Gaussians must be less than or equal to the number of unique words.'):
        task_func(text, num_gaussians=num_gaussians)

def test_task_func_with_seed():
    text = "apple banana apple [fruit] orange banana"
    seed = 42

    word_freqs_1, means_1 = task_func(text, seed=seed)
    word_freqs_2, means_2 = task_func(text, seed=seed)

    assert word_freqs_1 == word_freqs_2
    assert np.array_equal(means_1, means_2)