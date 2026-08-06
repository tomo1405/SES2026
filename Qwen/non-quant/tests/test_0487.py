import matplotlib.pyplot as plt
import numpy as np
import pytest
from src_0487 import task_func


def test_task_func_invalid_start_end():
    with pytest.raises(ValueError, match="Start time must be before end time"):
        task_func(1633072800000, 1633072800000, 60000, 0.1)

def test_task_func_invalid_step():
    with pytest.raises(ValueError, match="Invalid step value."):
        task_func(1633072800000, 1633076400000, 0, 0.1)

def test_task_func_valid_input():
    ax = task_func(1633072800000, 1633076400000, 60000, 0.1)
    assert isinstance(ax, plt.Axes)
    df = ax.get_lines()[0].get_data()
    assert len(df[0]) == 7
    assert len(df[1]) == 7

def test_task_func_random_values():
    np.random.seed(42)
    ax1 = task_func(1633072800000, 1633076400000, 60000, 0.1)
    np.random.seed(42)
    ax2 = task_func(1633072800000, 1633076400000, 60000, 0.1)
    df1 = ax1.get_lines()[0].get_data()
    df2 = ax2.get_lines()[0].get_data()
    assert np.array_equal(df1[1], df2[1])

def test_task_func_trend():
    ax = task_func(1633072800000, 1633076400000, 60000, 1.0)
    df = ax.get_lines()[0].get_data()
    assert df[1][-1] > df[1][0]