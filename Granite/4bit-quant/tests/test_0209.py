import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from src_0209 import task_func
import pytest

def test_task_func_valid_input():
    elements = 10
    seed = 0
    descriptive_stats, ax = task_func(elements, seed)
    assert isinstance(descriptive_stats, dict)
    assert isinstance(ax, plt.Axes)

def test_task_func_invalid_input():
    elements = "abc"
    seed = 0
    with pytest.raises(ValueError):
        task_func(elements, seed)

def test_task_func_seed_effect():
    elements = 10
    seed_1 = 0
    seed_2 = 1
    descriptive_stats_1, _ = task_func(elements, seed_1)
    descriptive_stats_2, _ = task_func(elements, seed_2)
    assert descriptive_stats_1 != descriptive_stats_2