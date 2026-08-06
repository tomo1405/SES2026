import pytest
from src_0844 import task_func

def test_task_func():
    # Test with n_sentences = 1
    n_sentences = 1
    expected_text = "sample text contains several words including."
    assert task_func(n_sentences) == expected_text

    # Test with n_sentences = 2
    n_sentences = 2
    expected_text = "sample text contains several words including. sample text contains several words including."
    assert task_func(n_sentences) == expected_text

    # Test with n_sentences = 3
    n_sentences = 3
    expected_text = "sample text contains several words including. sample text contains several words including. sample text contains several words including."
    assert task_func(n_sentences) == expected_text

    # Test with n_sentences = 4
    n_sentences = 4
    expected_text = "sample text contains several words including. sample text contains several words including. sample text contains several words including. sample text contains several words including."
    assert task_func(n_sentences) == expected_text

    # Test with n_sentences = 5
    n_sentences = 5
    expected_text = "sample text contains several words including. sample text contains several words including. sample text contains several words including. sample text contains several words including. sample text contains several words including."
    assert task_func(n_sentences) == expected_text