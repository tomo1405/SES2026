import random
import string

from src_0099 import task_func


def test_task_func():
    # Test with 0 strings
    result = task_func(0, 10)
    assert result == []

    # Test with 1 string of length 0
    result = task_func(1, 0)
    assert result == []

    # Test with 1 string of length 1
    result = task_func(1, 1)
    assert len(result) == 1 and all(isinstance(item, tuple) and len(item) == 2 for item in result)

    # Test with multiple strings of varying lengths
    result = task_func(5, 5)
    assert len(result) <= 26 and all(isinstance(item, tuple) and len(item) == 2 for item in result)

    # Test with a large number of strings and characters
    result = task_func(1000, 10)
    assert len(result) <= 26 and all(isinstance(item, tuple) and len(item) == 2 for item in result)

    # Test with all possible lowercase characters
    expected_characters = set(string.ascii_lowercase)
    result = task_func(len(expected_characters), 1)
    result_characters = {char for char, count in result}
    assert result_characters == expected_characters

    # Test with repeated characters
    result = task_func(10, 1)
    assert all(count >= 1 for _, count in result)

    # Test with a specific distribution of characters
    expected_distribution = [('a', 5), ('b', 3), ('c', 2)]
    random.seed(42)  # Ensure reproducibility
    result = task_func(10, 1)
    assert result[:3] == expected_distribution

    # Test with a non-ASCII character (should be ignored)
    random.seed(42)
    result = task_func(10, 1)
    assert all(char in string.ascii_lowercase for char, _ in result)