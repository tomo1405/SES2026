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
    # Test case 1: Test with an empty word
    expected_df = pd.DataFrame({'Letter': [], 'Position': []})
    actual_df = task_func('')
    assert actual_df.equals(expected_df)

    # Test case 2: Test with a word containing non-alphabetic characters
    with pytest.raises(ValueError):
        task_func('Hello!}')

    # Test case 3: Test with a word containing alphabetic characters
    expected_df = pd.DataFrame({'Letter': list('hello'), 'Position': [5, 4, 3, 2, 1]})
    actual_df = task_func('hello')
    assert actual_df.equals(expected_df)