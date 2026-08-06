import pytest
from src_0437 import task_func
import string
import matplotlib.pyplot as plt

def test_task_func():
    # Test with a simple string
    result, _ = task_func("hello world")
    assert result == {'a': 0, 'b': 0, 'c': 0, 'd': 1, 'e': 1, 'f': 0, 'g': 0, 'h': 1, 'i': 0, 'j': 0, 'k': 0, 'l': 1, 'm': 0, 'n': 0, 'o': 2, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

    # Test with a different string
    result, _ = task_func("hello world")
    assert result == {'a': 0, 'b': 0, 'c': 0, 'd': 1, 'e': 1, 'f': 0, 'g': 0, 'h': 1, 'i': 0, 'j': 0, 'k': 0, 'l': 1, 'm': 0, 'n': 0, 'o': 2, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

    # Test with an empty string
    result, _ = task_func("")
    assert result == {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

    # Test with a string containing only one letter
    result, _ = task_func("aaaaa")
    assert result == {'a': 5, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

    # Test with a string containing only one letter
    result, _ = task_func("b")
    assert result == {'a': 0, 'b': 1, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

    # Test with a string containing uppercase letters
    result, _ = task_func("Hello World")
    assert result == {'a': 0, 'b': 1, 'c': 0, 'd': 1, 'e': 1, 'f': 0, 'g': 0, 'h': 1, 'i': 0, 'j': 0, 'k': 0, 'l': 1, 'm': 0, 'n': 0, 'o': 1, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

pytest.main()