import pytest
from src_0983 import task_func
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def test_task_func():
    df = pd.DataFrame({"A": np.random.normal(0, 1, 100)})
    ax = task_func(df, "A")
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Normal Fit for 'A'"
    assert ax.get_ylabel() == "Density"
    assert ax.get_xlabel() == "A"
    assert ax.get_xlim() == (0, 1)
    assert ax.get_ylim() == (0, 1)
    assert ax.get_lines()[0].get_color() == "g"
    assert ax.get_lines()[0].get_linewidth() == 2
    assert ax.get_lines()[1].get_color() == "k"
    assert ax.get_lines()[1].get_linewidth() == 2

def test_task_func_with_bins():
    df = pd.DataFrame({"A": np.random.normal(0, 1, 100)})
    ax = task_func(df, "A", bins=50)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Normal Fit for 'A'"
    assert ax.get_ylabel() == "Density"
    assert ax.get_xlabel() == "A"
    assert ax.get_xlim() == (0, 1)
    assert ax.get_ylim() == (0, 1)
    assert ax.get_lines()[0].get_color() == "g"
    assert ax.get_lines()[0].get_linewidth() == 2
    assert ax.get_lines()[1].get_color() == "k"
    assert ax.get_lines()[1].get_linewidth() == 2

def test_task_func_with_density():
    df = pd.DataFrame({"A": np.random.normal(0, 1, 100)})
    ax = task_func(df, "A", density=False)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Normal Fit for 'A'"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_xlabel() == "A"
    assert ax.get_xlim() == (0, 1)
    assert ax.get_ylim() == (0, 1)
    assert ax.get_lines()[0].get_color() == "g"
    assert ax.get_lines()[0].get_linewidth() == 2
    assert ax.get_lines()[1].get_color() == "k"
    assert ax.get_lines()[1].get_linewidth() == 2

def test_task_func_with_alpha():
    df = pd.DataFrame({"A": np.random.normal(0, 1, 100)})
    ax = task_func(df, "A", alpha=0.8)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Normal Fit for 'A'"
    assert ax.get_ylabel() == "Density"
    assert ax.get_xlabel() == "A"
    assert ax.get_xlim() == (0, 1)
    assert ax.get_ylim() == (0, 1)
    assert ax.get_lines()[0].get_color() == "g"
    assert ax.get_lines()[0].get_linewidth() == 2
    assert ax.get_lines()[1].get_color() == "k"
    assert ax.get_lines()[1].get_linewidth() == 2

def test_task_func_with_color():
    df = pd.DataFrame({"A": np.random.normal(0, 1, 100)})
    ax = task_func(df, "A", color="r")
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Normal Fit for 'A'"
    assert ax.get_ylabel() == "Density"
    assert ax.get_xlabel() == "A"
    assert ax.get_xlim() == (0, 1)
    assert ax.get_ylim() == (0, 1)
    assert ax.get_lines()[0].get_color() == "r"
    assert ax.get_lines()[0].get_linewidth() == 2
    assert ax.get_lines()[1].get_color() == "k"
    assert ax.get_lines()[1].get_linewidth() == 2

def test_task_func_with_seed():
    df = pd.DataFrame({"A": np.random.normal(0, 1, 100)})
    ax = task_func(df, "A", seed=42)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Normal Fit for 'A'"
    assert ax.get_ylabel() == "Density"
    assert ax.get_xlabel() == "A"
    assert ax.get_xlim() == (0, 1)
    assert ax.get_ylim() == (0, 1)
    assert ax.get_lines()[0].get_color() == "g"
    assert ax.get_lines()[0].get_linewidth() == 2
    assert ax.get_lines()[1].get_color() == "k"
    assert ax.get_lines()[1].get_linewidth() == 2