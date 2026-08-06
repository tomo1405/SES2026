import pytest
from src_0558 import task_func
import numpy as np
from difflib import SequenceMatcher
import matplotlib.pyplot as plt
import os

def test_task_func_basic():
    s_list = ["hello", "world", "hi"]
    expected_avg_scores = [
        (SequenceMatcher(None, "hello", "world").ratio() + SequenceMatcher(None, "hello", "hi").ratio()) / 2,
        (SequenceMatcher(None, "world", "hello").ratio() + SequenceMatcher(None, "world", "hi").ratio()) / 2,
        (SequenceMatcher(None, "hi", "hello").ratio() + SequenceMatcher(None, "hi", "world").ratio()) / 2
    ]
    assert np.allclose(task_func(s_list), expected_avg_scores)

def test_task_func_single_element():
    s_list = ["test"]
    expected_avg_scores = [1.0]  # A string is perfectly similar to itself
    assert np.allclose(task_func(s_list), expected_avg_scores)

def test_task_func_empty_list():
    s_list = []
    expected_avg_scores = []
    assert np.allclose(task_func(s_list), expected_avg_scores)

def test_task_func_non_string_element():
    s_list = ["valid", 123, "string"]
    with pytest.raises(ValueError):
        task_func(s_list)

def test_task_func_plot():
    s_list = ["a", "b", "c"]
    plot_path = "test_plot.png"
    task_func(s_list, plot_path)
    assert os.path.exists(plot_path)
    os.remove(plot_path)  # Clean up the created file

def test_task_func_plot_not_provided():
    s_list = ["a", "b", "c"]
    task_func(s_list)  # No plot should be generated, so no need to check for file existence