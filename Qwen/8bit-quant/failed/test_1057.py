import pytest
from src_1057 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_default():
    bars = task_func()
    assert len(bars) == 26
    assert all(isinstance(bar, plt.Rectangle) for bar in bars)

def test_task_func_custom_pairs():
    bars = task_func(n_pairs=10)
    assert len(bars) == 10
    assert all(isinstance(bar, plt.Rectangle) for bar in bars)

def test_task_func_min_pairs():
    bars = task_func(n_pairs=1)
    assert len(bars) == 1
    assert all(isinstance(bar, plt.Rectangle) for bar in bars)

def test_task_func_max_pairs():
    bars = task_func(n_pairs=26)
    assert len(bars) == 26
    assert all(isinstance(bar, plt.Rectangle) for bar in bars)

def test_task_func_invalid_pairs():
    with pytest.raises(ValueError):
        task_func(n_pairs=0)
    with pytest.raises(ValueError):
        task_func(n_pairs=27)

def test_task_func_counts_range():
    bars = task_func()
    counts = [bar.get_height() for bar in bars]
    assert all(1 <= count <= 9 for count in counts)

def test_task_func_random_shuffle():
    bars1 = task_func()
    bars2 = task_func()
    labels1 = [bar.get_label() for bar in bars1]
    labels2 = [bar.get_label() for bar in bars2]
    assert labels1 != labels2

def test_task_func_plot_labels():
    bars = task_func()
    plt.gca().get_xlabel() == "Letter:Number Pairs"
    plt.gca().get_ylabel() == "Counts"
    plt.gca().get_title() == "Random Letter:Number Pairs Chart"