import matplotlib
import pytest
from src_1057 import task_func


def test_task_func_valid_input():
    bars = task_func(n_pairs=26)
    assert len(bars) == 26
    assert all(isinstance(bar, matplotlib.patches.Rectangle) for bar in bars)

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func(n_pairs=0)
    with pytest.raises(ValueError):
        task_func(n_pairs=27)

def test_task_func_randomness():
    bars1 = task_func(n_pairs=26)
    bars2 = task_func(n_pairs=26)
    assert not all(bar1 == bar2 for bar1, bar2 in zip(bars1, bars2))