python
import string
import random
import pytest

def replace_with_random_char(c):
    if c.isalpha():
        if c.islower():
            return random.choice(string.ascii_lowercase)
        else:
            return random.choice(string.ascii_uppercase)
    return c

def task_func(text, seed=None):
    if seed is not None:
        random.seed(seed)
    return "".join(replace_with_random_char(c) for c in text)

def test_task_func():
    # Test case 1: Replace all letters with random lowercase letters
    text = "Hello World"
    seed = 1234
    expected_result = "hEllO wOrld"
    result = task_func(text, seed)
    assert result == expected_result

    # Test case 2: Replace all letters with random uppercase letters
    text = "Hello World"
    seed = 5678
    expected_result = "hEllO wOrld"
    result = task_func(text, seed)
    assert result == expected_result

    # Test case 3: Replace all letters with random letters
    text = "Hello World"
    seed = None
    expected_result = "hEllO wOrld"
    result = task_func(text, seed)
    assert result == expected_result

    # Test case 4: Replace all letters with random letters with a given seed
    text = "Hello World"
    seed = 1234
    expected_result = "hEllO wOrld"
    result = task_func(text, seed)
    assert result == expected_result

    # Test case 5: Replace all letters with random letters with a different seed
    text = "Hello World"
    seed = 5678
    expected_result = "hEllO wOrld"
    result = task_func(text, seed)
    assert result == expected_result

    # Test case 6: Replace all letters with random letters with a different seed
    text = "Hello World"
    seed = 9012
    expected_result = "hEllO wOrld"
    result = task_func(text, seed)
    assert result == expected_result

    # Test case 7: Replace all letters with random letters with a different seed
    text = "Hello World"
    seed = 3456
    expected_result = "hEllO wOrld"
    result = task_func(text, seed)
    assert result == expected_result

    # Test case 8: Replace all letters with random letters with a different seed
    text = "Hello World"
    seed = 7890
    expected_result = "hEllO wOrld"
    result = task_func(text, seed)
    assert result == expected_result

    # Test case 9: Replace all letters with random letters with a different seed
    text = "Hello World"
    seed = 4567
    expected_result = "hEllO wOrld"
    result = task_func(text, seed)
    assert result == expected_result

    # Test case 10: Replace all letters with random letters with a different seed
    text = "Hello World"
    seed = 8901
    expected_result = "hEllO wOrld"
    result = task_func(text, seed)
    assert result == expected_result