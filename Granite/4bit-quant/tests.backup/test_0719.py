import re
import numpy as np
from scipy.stats import ttest_rel
def task_func(text1, text2):
    word_counts1 = np.array([len(word) for word in re.split(r'\W+', text1) if word])
    word_counts2 = np.array([len(word) for word in re.split(r'\W+', text2) if word])

    if len(word_counts1) != len(word_counts2):
        return (np.nan, np.nan)

    t_statistic, p_value = ttest_rel(word_counts1, word_counts2)
    return t_statistic, p_value
import pytest

def test_task_func():
    # Test case 1: text1 and text2 have the same number of words
    text1 = "This is a test"
    text2 = "This is a test"
    expected_output = (0.0, 1.0)
    actual_output = task_func(text1, text2)
    assert actual_output == expected_output, "Test case 1 failed"

    # Test case 2: text1 and text2 have different number of words
    text1 = "This is a test"
    text2 = "This is a test with more words"
    expected_output = (0.0, 0.05234444753661772)
    actual_output = task_func(text1, text2)
    assert actual_output == expected_output, "Test case 2 failed"

if __name__ == "__main__":
    pytest.main()