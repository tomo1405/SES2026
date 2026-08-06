import pytest
from src_1086 import task_func
import re
from collections import Counter
import matplotlib.pyplot as plt

def test_task_func():
    # Test with a sample text
    text = "This is a test. This test is only a test."
    expected_words = [('test', 2), ('this', 2), ('is', 2), ('a', 2)]
    result, _ = task_func(text)
    assert result == expected_words

    # Add more test cases as needed