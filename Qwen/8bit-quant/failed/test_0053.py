import pytest
from src_0053 import task_func
import pandas as pd

def test_task_func():
    # Test with a simple sentence
    text = "The quick brown fox jumps over the lazy dog"
    expected_output = pd.Series({'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1})
    assert task_func(text).equals(expected_output)

    # Test with multiple sentences and punctuation
    text = "Hello, world! Hello universe."
    expected_output = pd.Series({'hello': 2, 'world': 1, 'universe': 1})
    assert task_func(text).equals(expected_output)

    # Test with stopwords only
    text = "a an the in is are"
    expected_output = pd.Series(dtype=int)
    assert task_func(text).equals(expected_output)

    # Test with empty string
    text = ""
    expected_output = pd.Series(dtype=int)
    assert task_func(text).equals(expected_output)

    # Test with case insensitivity
    text = "THE quick BROWN fox"
    expected_output = pd.Series({'quick': 1, 'brown': 1, 'fox': 1})
    assert task_func(text).equals(expected_output)

    # Test with numbers and symbols
    text = "123 the quick brown fox! 456"
    expected_output = pd.Series({'quick': 1, 'brown': 1, 'fox': 1})
    assert task_func(text).equals(expected_output)