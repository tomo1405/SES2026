python
import re
import numpy as np
from scipy.stats import ttest_rel
import pytest

def task_func(text1, text2):
    word_counts1 = np.array([len(word) for word in re.split(r'\W+', text1) if word])
    word_counts2 = np.array([len(word) for word in re.split(r'\W+', text2) if word])

    if len(word_counts1) != len(word_counts2):
        return (np.nan, np.nan)

    t_statistic, p_value = ttest_rel(word_counts1, word_counts2)
    return t_statistic, p_value

def test_task_func():
    # Test case 1
    text1 = "The quick brown fox jumps over the lazy dog."
    text2 = "The quick brown dog jumps over the lazy fox."
    expected_t_statistic = 0.0001
    expected_p_value = 0.9999
    t_statistic, p_value = task_func(text1, text2)
    assert abs(t_statistic - expected_t_statistic) < 1e-4
    assert abs(p_value - expected_p_value) < 1e-4

    # Test case 2
    text1 = "The quick brown fox jumps over the lazy dog."
    text2 = "The quick brown dog jumps over the lazy fox."
    expected_t_statistic = 0.0001
    expected_p_value = 0.9999
    t_statistic, p_value = task_func(text1, text2)
    assert abs(t_statistic - expected_t_statistic) < 1e-4
    assert abs(p_value - expected_p_value) < 1e-4

    # Test case 3
    text1 = "The quick brown fox jumps over the lazy dog."
    text2 = "The quick brown dog jumps over the lazy fox."
    expected_t_statistic = 0.0001
    expected_p_value = 0.9999
    t_statistic, p_value = task_func(text1, text2)
    assert abs(t_statistic - expected_t_statistic) < 1e-4
    assert abs(p_value - expected_p_value) < 1e-4

    # Test case 4
    text1 = "The quick brown fox jumps over the lazy dog."
    text2 = "The quick brown dog jumps over the lazy fox."
    expected_t_statistic = 0.0001
    expected_p_value = 0.9999
    t_statistic, p_value = task_func(text1, text2)
    assert abs(t_statistic - expected_t_statistic) < 1e-4
    assert abs(p_value - expected_p_value) < 1e-4

    # Test case 5
    text1 = "The quick brown fox jumps over the lazy dog."
    text2 = "The quick brown dog jumps over the lazy fox."
    expected_t_statistic = 0.0001
    expected_p_value = 0.9999
    t_statistic, p_value = task_func(text1, text2)
    assert abs(t_statistic - expected_t_statistic) < 1e-4
    assert abs(p_value - expected_p_value) < 1e-4

    # Test case 6
    text1 = "The quick brown fox jumps over the lazy dog."
    text2 = "The quick brown dog jumps over the lazy fox."
    expected_t_statistic = 0.0001
    expected_p_value = 0.9999
    t_statistic, p_value = task_func(text1, text2)
    assert abs(t_statistic - expected_t_statistic) < 1e-4
    assert abs(p_value - expected_p_value) < 1e-4

    # Test case 7
    text1 = "The quick brown fox jumps over the lazy dog."
    text2 = "The quick brown dog jumps over the lazy fox."
    expected_t_statistic = 0.0001
    expected_p_value = 0.9999
    t_statistic, p_value = task_func(text1, text2)
    assert abs(t_statistic - expected_t_statistic) < 1e-4
    assert abs(p_value - expected_p_value) < 1e-4

    # Test case 8
    text1 = "The quick brown fox jumps over the lazy dog."
    text2 = "The quick brown dog jumps over the lazy fox."
    expected_t_statistic = 0.0001
    expected_p_value = 0.9999
    t_statistic, p_value = task_func(text1, text2)
    assert abs(t_statistic - expected_t_statistic) < 1e-4
    assert abs(p_value - expected_p_value) < 1e-4

    # Test case 9
    text1 = "The quick brown fox jumps over the lazy dog."
    text2 = "The quick brown dog jumps over the lazy fox."
    expected_t_statistic = 0.0001
    expected_p_value = 0.9999
    t_statistic, p_value = task_func(text1, text2)
    assert abs(t_statistic - expected_t_statistic) < 1e-4
    assert abs(p_value - expected_p_value) < 1e-4

    # Test case 10
    text1 = "The quick brown fox jumps over the lazy dog."
    text2 = "The quick brown dog jumps over the lazy fox."
    expected_t_statistic = 0.0001
    expected_p_value = 0.9999
    t_statistic, p_value = task_func(text1, text2)
    assert abs(t_statistic - expected_t_statistic) < 1e-4
    assert abs(p_value - expected_p_value) < 1e-4