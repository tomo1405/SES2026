import pytest
from src_0324 import task_func

def test_task_func():
    text = "Hello [World], how are you?"
    num_gaussians = 2
    seed = 42
    expected_word_freqs = {'Hello': 1, 'World': 1, 'how': 1, 'are': 1, 'you': 1}
    expected_means = [1, 1]

    word_freqs, means = task_func(text, num_gaussians, seed)

    assert word_freqs == expected_word_freqs
    assert means == expected_means

def test_task_func_invalid_num_gaussians():
    text = "Hello [World], how are you?"
    num_gaussians = 0
    seed = 42

    with pytest.raises(ValueError):
        task_func(text, num_gaussians, seed)

def test_task_func_invalid_num_words():
    text = "Hello [World], how are you?"
    num_gaussians = 5
    seed = 42

    with pytest.raises(Exception):
        task_func(text, num_gaussians, seed)