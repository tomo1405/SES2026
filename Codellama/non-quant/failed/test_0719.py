import pytest
from src_0719 import task_func

def test_task_func():
    text1 = "This is a sample text"
    text2 = "This is another sample text"
    expected_t_statistic = 0.0
    expected_p_value = 1.0

    t_statistic, p_value = task_func(text1, text2)

    assert t_statistic == expected_t_statistic
    assert p_value == expected_p_value

def test_task_func_different_lengths():
    text1 = "This is a sample text"
    text2 = "This is another sample text with extra words"
    expected_t_statistic = np.nan
    expected_p_value = np.nan

    t_statistic, p_value = task_func(text1, text2)

    assert t_statistic == expected_t_statistic
    assert p_value == expected_p_value