import pandas as pd
import re
from scipy import stats
from src_0322 import task_func
import pytest

def test_task_func():
    # Test case 1: No names found in the text
    text1 = "This is a sample text without any names."
    expected_output1 = (pd.Series(), None, None, None)
    actual_output1 = task_func(text1)
    assert actual_output1 == expected_output1, "Test case 1 failed: Expected output does not match actual output."

    # Test case 2: Names found in the text
    text2 = "John[123], Jane[456], and Bob are the names in this text."
    expected_output2 = (pd.Series(['John': 1, 'Jane': 1, 'Bob': 1]), ax, skewness, kurtosis)
    actual_output2 = task_func(text2)
    assert actual_output2 == expected_output2, "Test case 2 failed: Expected output does not match actual output."

    # Test case 3: Names with special characters and whitespaces
    text3 = "Alice[123], Bob [456], and Eve\tare the names in this text."
    expected_output3 = (pd.Series(['Alice': 1, 'Bob': 1, 'Eve': 1]), ax, skewness, kurtosis)
    actual_output3 = task_func(text3)
    assert actual_output3 == expected_output3, "Test case 3 failed: Expected output does not match actual output."