import pytest
from src_0324 import task_func

def test_task_func_basic():
    text = "apple [fruit] banana apple orange banana"
    expected_word_freqs = {'apple': 2, 'banana': 2, 'orange': 1}
    word_freqs, means = task_func(text, num_gaussians=3)
    assert word_freqs == expected_word_freqs
    assert means.shape == (3, 1)

def test_task_func_single_gaussian():
    text = "cat dog cat"
    expected_word_freqs = {'cat': 2, 'dog': 1}
    word_freqs, means = task_func(text, num_gaussians=1)
    assert word_freqs == expected_word_freqs
    assert means.shape == (1, 1)

def test_task_func_no_gaussians():
    text = "hello world"
    with pytest.raises(ValueError):
        task_func(text, num_gaussians=0)

def test_task_func_more_gaussians_than_unique_words():
    text = "one two three"
    with pytest.raises(Exception):
        task_func(text, num_gaussians=4)

def test_task_func_with_seed():
    text = "repeat repeat repeat"
    word_freqs_1, means_1 = task_func(text, seed=42)
    word_freqs_2, means_2 = task_func(text, seed=42)
    assert word_freqs_1 == word_freqs_2
    assert np.array_equal(means_1, means_2)

def test_task_func_with_brackets():
    text = "alpha [bracket] beta [bracket] gamma"
    expected_word_freqs = {'alpha': 1, 'beta': 1, 'gamma': 1}
    word_freqs, means = task_func(text, num_gaussians=3)
    assert word_freqs == expected_word_freqs
    assert means.shape == (3, 1)