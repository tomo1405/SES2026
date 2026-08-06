python
import pandas as pd
import string
import pytest

def task_func(word):
    if not word:  # Check if the input word is empty and return an empty DataFrame
        return pd.DataFrame({'Letter': [], 'Position': []})
    elif not word.isalpha() or not word.islower():
        raise ValueError("Input word must be in lowercase alphabetic characters only.")

    alphabet = string.ascii_lowercase
    positions = [alphabet.index(char) + 1 for char in word]
    df = pd.DataFrame({'Letter': list(word), 'Position': positions})

    return df

def test_task_func():
    # Test case 1: Empty input word
    assert task_func('') == pd.DataFrame({'Letter': [], 'Position': []})

    # Test case 2: Input word with invalid characters
    with pytest.raises(ValueError):
        task_func('Hello')

    # Test case 3: Input word with valid characters
    assert task_func('python') == pd.DataFrame({'Letter': ['p', 'y', 't', 'h', 'o', 'n'], 'Position': [1, 2, 3, 4, 5, 6]})