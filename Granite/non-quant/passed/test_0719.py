import re
import numpy as np
from scipy.stats import ttest_rel
from src_0719 import task_func
import pytest

def test_task_func():
    # Test case 1: Both text1 and text2 have at least one word
    text1 = "This is a sample text"
    text2 = "Another sample text"
    expected_output = (0.0, 1.0)  # t_statistic, p_value
    actual_output = task_func(text1, text2)
    assert actual_output == expected_output

    # Test case 2: text1 has no words, text2 has at least one word
    text1 = ""
    text2 = "Another sample text"
    expected_output = (np.nan, np.nan)
    actual_output = task_func(text1, text2)
    assert actual_output == expected_output

    # Test case 3: text1 has at least one word, text2 has no words
    text1 = "This is a sample text"
    text2 = ""
    expected_output = (np.nan, np.nan)
    actual_output = task_func(text1, text2)
    assert actual_output == expected_output

    # Test case 4: Both text1 and text2 have no words
    text1 = ""
    text2 = ""
    expected_output = (np.nan, np.nan)
    actual_output = task_func(text1, text2)
    assert actual_output == expected_output