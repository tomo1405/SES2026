import pytest
from src_0558 import task_func
import numpy as np
import matplotlib.pyplot as plt
from difflib import SequenceMatcher

def test_task_func_valid_input():
    s_list = ["hello", "world", "python"]
    expected_output = [0.5, 0.5, 0.5]
    assert task_func(s_list) == expected_output

def test_task_func_invalid_input():
    s_list = ["hello", 123, "world"]
    with pytest.raises(ValueError):
        task_func(s_list)

def test_task_func_plot_output():
    s_list = ["hello", "world", "python"]
    plot_path = "plot.png"
    task_func(s_list, plot_path=plot_path)
    assert os.path.exists(plot_path)