import numpy as np
from src_0719 import task_func


def test_task_func_equal_texts():
    text1 = "Hello world"
    text2 = "Hello world"
    t_statistic, p_value = task_func(text1, text2)
    assert np.isnan(t_statistic)
    assert np.isnan(p_value)

def test_task_func_different_texts():
    text1 = "Hello world"
    text2 = "Goodbye world"
    t_statistic, p_value = task_func(text1, text2)
    assert not np.isnan(t_statistic)
    assert not np.isnan(p_value)

def test_task_func_empty_texts():
    text1 = ""
    text2 = ""
    t_statistic, p_value = task_func(text1, text2)
    assert np.isnan(t_statistic)
    assert np.isnan(p_value)

def test_task_func_one_empty_text():
    text1 = "Hello world"
    text2 = ""
    t_statistic, p_value = task_func(text1, text2)
    assert np.isnan(t_statistic)
    assert np.isnan(p_value)

def test_task_func_different_word_counts():
    text1 = "Hello world"
    text2 = "Goodbye"
    t_statistic, p_value = task_func(text1, text2)
    assert np.isnan(t_statistic)
    assert np.isnan(p_value)

def test_task_func_identical_words():
    text1 = "a a a a"
    text2 = "a a a a"
    t_statistic, p_value = task_func(text1, text2)
    assert np.isnan(t_statistic)
    assert np.isnan(p_value)

def test_task_func_different_word_lengths():
    text1 = "short long longer"
    text2 = "tiny big huge"
    t_statistic, p_value = task_func(text1, text2)
    assert not np.isnan(t_statistic)
    assert not np.isnan(p_value)