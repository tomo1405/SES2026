import pytest
from src_0637 import task_func
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def test_task_func_zero_rows():
    df, ax = task_func(0)
    assert isinstance(df, pd.DataFrame)
    assert df.empty
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Non-Zero Value Counts'

def test_task_func_negative_rows():
    df, ax = task_func(-5)
    assert isinstance(df, pd.DataFrame)
    assert df.empty
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Non-Zero Value Counts'

def test_task_func_positive_rows():
    rows = 10
    df, ax = task_func(rows)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (rows, len(COLUMNS))
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Non-Zero Value Counts'
    assert all(count >= 0 for count in df.astype(bool).sum(axis=0))

def test_task_func_plot_data():
    rows = 10
    df, ax = task_func(rows)
    counts = df.astype(bool).sum(axis=0)
    bars = ax.patches
    assert len(bars) == len(COLUMNS)
    for i, bar in enumerate(bars):
        assert bar.get_height() == counts[i]

def test_task_func_plot_labels():
    rows = 10
    _, ax = task_func(rows)
    assert ax.get_xlabel() == 'COLUMNS'
    assert ax.get_ylabel() == 'Counts'