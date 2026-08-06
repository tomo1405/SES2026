import numpy as np
from src_0719 import task_func


def test_task_func():
    text1 = "This is a test sentence."
    text2 = "This is another test sentence."
    expected_word_counts1 = np.array([3, 3, 2, 1])
    expected_word_counts2 = np.array([3, 3, 2, 1])
    expected_t_statistic = 0.0
    expected_p_value = 1.0

    word_counts1, word_counts2 = task_func(text1, text2)
    assert np.array_equal(word_counts1, expected_word_counts1)
    assert np.array_equal(word_counts2, expected_word_counts2)
    t_statistic, p_value = task_func(word_counts1, word_counts2)
    assert t_statistic == expected_t_statistic
    assert p_value == expected_p_value

def test_task_func_unequal_length():
    text1 = "This is a test sentence."
    text2 = "This is another test sentence. This is a third sentence."
    expected_word_counts1 = np.array([3, 3, 2, 1])
    expected_word_counts2 = np.array([3, 3, 2, 1, 3])
    expected_t_statistic = np.nan
    expected_p_value = np.nan

    word_counts1, word_counts2 = task_func(text1, text2)
    assert np.array_equal(word_counts1, expected_word_counts1)
    assert np.array_equal(word_counts2, expected_word_counts2)
    t_statistic, p_value = task_func(word_counts1, word_counts2)
    assert t_statistic == expected_t_statistic
    assert p_value == expected_p_value