import pytest
from src_0959 import task_func

def test_task_func():
    # Test with no seed
    text = "The quick brown fox jumps over the lazy dog."
    expected_result = "The qick brown fox jumps over the lazy dog."
    assert task_func(text) == expected_result

    # Test with seed
    text = "The quick brown fox jumps over the lazy dog."
    seed = 1234
    expected_result = "The qick brown fox jumps over the lazy dog."
    assert task_func(text, seed) == expected_result

    # Test with different text
    text = "The quick brown fox jumps over the lazy dog."
    expected_result = "The qick brown fox jumps over the lazy dog."
    assert task_func(text) == expected_result

    # Test with different seed
    text = "The quick brown fox jumps over the lazy dog."
    seed = 5678
    expected_result = "The qick brown fox jumps over the lazy dog."
    assert task_func(text, seed) == expected_result

    # Test with different text and seed
    text = "The quick brown fox jumps over the lazy dog."
    seed = 9012
    expected_result = "The qick brown fox jumps over the lazy dog."
    assert task_func(text, seed) == expected_result