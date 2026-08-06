import pandas as pd
import pytest
from src_0936 import task_func


def test_task_func():
    # Test 1: Empty input
    word = ''
    expected_output = pd.DataFrame({'Letter': [], 'Position': []})
    assert task_func(word).equals(expected_output)

    # Test 2: Non-empty input
    word = 'hello'
    expected_output = pd.DataFrame({'Letter': ['h', 'e', 'l', 'l', 'o'], 'Position': [1, 2, 3, 4, 5]})
    assert task_func(word).equals(expected_output)

    # Test 3: Input with non-alphabetic characters
    word = 'hello123'
    with pytest.raises(ValueError):
        task_func(word)

    # Test 4: Input with uppercase characters
    word = 'Hello'
    with pytest.raises(ValueError):
        task_func(word)