import pytest
from src_0637 import task_func
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def test_task_func_zero_rows():
    df, ax = task_func(0)
    assert df.empty
    assert isinstance(df, pd.DataFrame)
    assert ax.get_title() == 'Non-Zero Value Counts'
    assert len(ax.patches) == 0

def test_task_func_negative_rows():
    df, ax = task_func(-5)
    assert df.empty
    assert isinstance(df, pd.DataFrame)
    assert ax.get_title() == 'Non-Zero Value Counts'
    assert len(ax.patches) == 0

def test_task_func_positive_rows():
    rows = 10
    df, ax = task_func(rows)
    assert not df.empty
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (rows, 5)
    assert ax.get_title() == 'Non-Zero Value Counts'
    assert len(ax.patches) == 5

def test_task_func_counts_correctness():
    rows = 10
    df, ax = task_func(rows)
    counts = df.astype(bool).sum(axis=0)
    for i, patch in enumerate(ax.patches):
        assert patch.get_height() == counts.iloc[i]

def test_task_func_plot_closing():
    plt.figure()
    task_func(0)
    assert len(plt.get_fignums()) == 0

def test_task_func_plot_titles():
    _, ax = task_func(0)
    assert ax.get_title() == 'Non-Zero Value Counts'
    _, ax = task_func(10)
    assert ax.get_title() == 'Non-Zero Value Counts'