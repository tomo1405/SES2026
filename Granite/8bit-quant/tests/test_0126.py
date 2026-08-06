import json

import pytest
from src_0126 import task_func


def test_task_func():
    # Test case 1: Check if the function returns a valid filename
    result = task_func(LETTERS, n)
    assert isinstance(result, str) and result.endswith('.json')

    # Test case 2: Check if the letter counts are correct
    result = task_func(LETTERS, n)
    with open(result, 'r') as f:
        letter_counts = json.load(f)
    for letter in LETTERS:
        assert letter_counts[letter] == n

    # Test case 3: Check if the function raises an error for invalid input
    with pytest.raises(ValueError):
        task_func(LETTERS, -1)