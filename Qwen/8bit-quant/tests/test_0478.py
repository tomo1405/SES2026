import pytest
from src_0478 import task_func
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func_default_parameters():
    df, ax = task_func()
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert len(df) == 100
    assert set(df['category'].unique()) == set(["A", "B", "C", "D", "E"])

def test_task_func_custom_N():
    df, ax = task_func(N=50)
    assert len(df) == 50
    assert set(df['category'].unique()) == set(["A", "B", "C", "D", "E"])

def test_task_func_custom_categories():
    df, ax = task_func(CATEGORIES=["X", "Y", "Z"])
    assert set(df['category'].unique()) == set(["X", "Y", "Z"])

def test_task_func_custom_seed():
    df1, _ = task_func(seed=123)
    df2, _ = task_func(seed=123)
    assert df1.equals(df2)

def test_task_func_N_less_than_categories():
    df, ax = task_func(N=3, CATEGORIES=["A", "B", "C", "D", "E"])
    assert len(df) == 3
    assert set(df['category'].unique()) == set(df['category'])

def test_task_func_N_greater_than_categories():
    df, ax = task_func(N=10, CATEGORIES=["A", "B", "C"])
    assert len(df) == 10
    assert set(df['category'].unique()) == set(["A", "B", "C"])

def test_task_func_plot_labels():
    df, ax = task_func()
    for category in ["A", "B", "C", "D", "E"]:
        assert category in ax.get_legend().get_texts()

def test_task_func_plot_data_points():
    df, ax = task_func(N=5)
    for category in ["A", "B", "C", "D", "E"]:
        points = ax.collections[0].get_offsets()[df['category'] == category]
        assert len(points) == df[df['category'] == category].shape[0]