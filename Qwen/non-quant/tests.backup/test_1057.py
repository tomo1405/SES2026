import pytest
from src_1057 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_default():
    bars = task_func()
    assert len(bars) == 26
    assert all(isinstance(bar, plt.Rectangle) for bar in bars)

def test_task_func_n_pairs_1():
    bars = task_func(n_pairs=1)
    assert len(bars) == 1
    assert isinstance(bars[0], plt.Rectangle)

def test_task_func_n_pairs_26():
    bars = task_func(n_pairs=26)
    assert len(bars) == 26
    assert all(isinstance(bar, plt.Rectangle) for bar in bars)

def test_task_func_invalid_n_pairs():
    with pytest.raises(ValueError):
        task_func(n_pairs=27)
    with pytest.raises(ValueError):
        task_func(n_pairs=0)

def test_task_func_random_shuffle():
    bars1 = task_func()
    bars2 = task_func()
    assert bars1 != bars2

def test_task_func_counts_range():
    bars = task_func()
    counts = [bar.get_height() for bar in bars]
    assert all(1 <= count <= 9 for count in counts)

def test_task_func_labels():
    bars = task_func()
    labels = [bar.get_label() for bar in bars]
    assert labels == [f"{letter}:{number}" for letter, number in zip("abcdefghijklmnopqrstuvwxyz", range(1, 27))]

def test_task_func_plot_titles():
    bars = task_func()
    ax = plt.gca()
    assert ax.get_xlabel() == "Letter:Number Pairs"
    assert ax.get_ylabel() == "Counts"
    assert ax.get_title() == "Random Letter:Number Pairs Chart"