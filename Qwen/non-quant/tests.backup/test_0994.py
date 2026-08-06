import pytest
from src_0994 import task_func
import matplotlib.pyplot as plt
import numpy as np

def test_task_func_empty_text():
    ax = task_func("")
    assert ax.has_data() == False

def test_task_func_single_word():
    ax = task_func("hello")
    assert ax.has_data() == True
    lines, labels = ax.get_legend_handles_labels()
    assert len(lines) == 1  # Only histogram
    assert len(labels) == 1

def test_task_func_multiple_words():
    ax = task_func("hello world")
    assert ax.has_data() == True
    lines, labels = ax.get_legend_handles_labels()
    assert len(lines) == 2  # Histogram and KDE
    assert len(labels) == 2

def test_task_func_no_variance():
    ax = task_func("aaaaa aaaaa")
    assert ax.has_data() == True
    lines, labels = ax.get_legend_handles_labels()
    assert len(lines) == 1  # Only histogram
    assert len(labels) == 1

def test_task_func_singular_matrix_error():
    ax = task_func("a" * 1000)
    assert ax.has_data() == True
    lines, labels = ax.get_legend_handles_labels()
    assert len(lines) == 1  # Only histogram
    assert len(labels) == 1

def test_task_func_non_alphanumeric_characters():
    ax = task_func("hello!@# $%^&*()")
    assert ax.has_data() == True
    lines, labels = ax.get_legend_handles_labels()
    assert len(lines) == 1  # Only histogram
    assert len(labels) == 1