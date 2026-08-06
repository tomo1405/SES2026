import pytest
from src_0929 import task_func

def test_task_func():
    # Test with an empty string
    assert task_func("") == {}

    # Test with a single character
    assert task_func("a") == {}

    # Test with a word that has no repeating characters
    assert task_func("abc") == {'ab': 1, 'bc': 1, 'aa': 0, 'bb': 0, 'cc': 0}

    # Test with a word that has repeating characters
    assert task_func("aabb") == {'ab': 2, 'ba': 1, 'aa': 2, 'bb': 2}

    # Test with a word that has all unique two-letter combinations
    assert task_func("abcdefgh") == {'ab': 1, 'bc': 1, 'cd': 1, 'de': 1, 'ef': 1, 'fg': 1, 'gh': 1, 'aa': 0, 'bb': 0, 'cc': 0, 'dd': 0, 'ee': 0, 'ff': 0, 'gg': 0, 'hh': 0}

    # Test with a word that has some repeated two-letter combinations
    assert task_func("aabbcc") == {'ab': 2, 'bc': 2, 'ca': 1, 'aa': 2, 'bb': 2, 'cc': 2}

    # Test with a word that has special characters
    assert task_func("a!b@c#d$") == {'a!': 1, '!b': 1, 'b@': 1, '@c': 1, 'c#': 1, '#d': 1, 'd$': 1, 'aa': 0, 'bb': 0, 'cc': 0, 'dd': 0}

    # Test with a word that has numbers
    assert task_func("123456") == {'12': 1, '23': 1, '34': 1, '45': 1, '56': 1, '11': 0, '22': 0, '33': 0, '44': 0, '55': 0, '66': 0}

    # Test with a word that has mixed case letters
    assert task_func("AbCdEfGh") == {'Ab': 1, 'bC': 1, 'Cd': 1, 'dE': 1, 'Ef': 1, 'fG': 1, 'gH': 1, 'AA': 0, 'BB': 0, 'CC': 0, 'DD': 0, 'EE': 0, 'FF': 0, 'GG': 0, 'HH': 0}