import pytest
from src_0957 import task_func

def test_task_func():
    # Test case 1: No seed provided
    text = "Hello, World!"
    expected = "HEllo, WOrld!"
    assert task_func(text) == expected

    # Test case 2: Seed provided
    text = "Hello, World!"
    seed = 1234
    expected = "HEllo, WOrld!"
    assert task_func(text, seed) == expected

    # Test case 3: No punctuation
    text = "Hello World"
    expected = "HEllo WOrld"
    assert task_func(text) == expected

    # Test case 4: No punctuation, seed provided
    text = "Hello World"
    seed = 1234
    expected = "HEllo WOrld"
    assert task_func(text, seed) == expected

    # Test case 5: No punctuation, seed provided, different text
    text = "Goodbye World"
    seed = 1234
    expected = "GdBye WOrld"
    assert task_func(text, seed) == expected

    # Test case 6: No punctuation, seed provided, different text
    text = "Hello World"
    seed = 5678
    expected = "HEllo WOrld"
    assert task_func(text, seed) == expected

    # Test case 7: No punctuation, seed provided, different text
    text = "Goodbye World"
    seed = 5678
    expected = "GdBye WOrld"
    assert task_func(text, seed) == expected

    # Test case 8: No punctuation, seed provided, different text
    text = "Hello World"
    seed = 9012
    expected = "HEllo WOrld"
    assert task_func(text, seed) == expected

    # Test case 9: No punctuation, seed provided, different text
    text = "Goodbye World"
    seed = 9012
    expected = "GdBye WOrld"
    assert task_func(text, seed) == expected

    # Test case 10: No punctuation, seed provided, different text
    text = "Hello World"
    seed = 3456
    expected = "HEllo WOrld"
    assert task_func(text, seed) == expected

    # Test case 11: No punctuation, seed provided, different text
    text = "Goodbye World"
    seed = 3456
    expected = "GdBye WOrld"
    assert task_func(text, seed) == expected

    # Test case 12: No punctuation, seed provided, different text
    text = "Hello World"
    seed = 7890
    expected = "HEllo WOrld"
    assert task_func(text, seed) == expected

    # Test case 13: No punctuation, seed provided, different text
    text = "Goodbye World"
    seed = 7890
    expected = "GdBye WOrld"
    assert task_func(text, seed) == expected

    # Test case 14: No punctuation, seed provided, different text
    text = "Hello World"
    seed = 101112
    expected = "HEllo WOrld"
    assert task_func(text, seed) == expected

    # Test case 15: No punctuation, seed provided, different text
    text = "Goodbye World"
    seed = 101112
    expected = "GdBye WOrld"
    assert task_func(text, seed) == expected