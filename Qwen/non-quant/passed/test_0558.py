import pytest
from src_0558 import task_func
import numpy as np
from difflib import SequenceMatcher
import matplotlib.pyplot as plt
import os

def test_task_func_no_plot():
    s_list = ["apple", "banana", "cherry"]
    expected_avg_scores = [
        (SequenceMatcher(None, "apple", "banana").ratio() + SequenceMatcher(None, "apple", "cherry").ratio()) / 2,
        (SequenceMatcher(None, "banana", "apple").ratio() + SequenceMatcher(None, "banana", "cherry").ratio()) / 2,
        (SequenceMatcher(None, "cherry", "apple").ratio() + SequenceMatcher(None, "cherry", "banana").ratio()) / 2
    ]
    assert np.allclose(task_func(s_list), expected_avg_scores)

def test_task_func_with_plot(tmpdir):
    s_list = ["apple", "banana", "cherry"]
    plot_path = str(tmpdir / "test_plot.png")
    task_func(s_list, plot_path=plot_path)
    assert os.path.exists(plot_path)

def test_task_func_non_string_items():
    s_list = ["apple", 123, "cherry"]
    with pytest.raises(ValueError, match="All items in s_list must be strings."):
        task_func(s_list)

def test_task_func_empty_list():
    s_list = []
    expected_avg_scores = []
    assert task_func(s_list) == expected_avg_scores

def test_task_func_single_item():
    s_list = ["apple"]
    expected_avg_scores = [0.0]  # No comparison possible, so average is 0
    assert task_func(s_list) == expected_avg_scores