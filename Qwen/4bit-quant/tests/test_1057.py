import matplotlib.pyplot as plt
import pytest
from src_1057 import task_func


def test_task_func_default():
    bars = task_func()
    assert len(bars) == 26
    assert all(isinstance(bar, plt.Rectangle) for bar in bars)

def test_task_func_n_pairs():
    bars = task_func(n_pairs=10)
    assert len(bars) == 10
    assert all(isinstance(bar, plt.Rectangle) for bar in bars)

def test_task_func_invalid_n_pairs():
    with pytest.raises(ValueError):
        task_func(n_pairs=27)
    with pytest.raises(ValueError):
        task_func(n_pairs=0)

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
    for bar, pair in zip(bars, sorted(LETTERS[:26])):
        assert bar.get_label() == f"{pair}:{LETTERS.index(pair) + 1}"