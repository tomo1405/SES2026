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

    # Test case 2: Input word with non-alphabetic characters
    with pytest.raises(ValueError):
        task_func('123')

    # Test case 3: Input word with uppercase characters
    with pytest.raises(ValueError):
        task_func('Abc')

    # Test case 4: Input word with lowercase characters
    assert task_func('abc') == pd.DataFrame({'Letter': ['a', 'b', 'c'], 'Position': [1, 2, 3]})

    # Test case 5: Input word with multiple occurrences of the same character
    assert task_func('aabbc') == pd.DataFrame({'Letter': ['a', 'a', 'b', 'b', 'c'], 'Position': [1, 2, 1, 2, 3]})