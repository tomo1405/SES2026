import pytest
from src_0236 import task_func
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols

def test_task_func_output_type():
    ax = task_func(mu=0, sigma=1)
    assert isinstance(ax, plt.Axes)

def test_task_func_histogram():
    ax = task_func(mu=0, sigma=1)
    lines = ax.get_lines()
    assert len(lines) == 2, "There should be two lines in the plot: one for the histogram and one for the fitted curve."

def test_task_func_histogram_data():
    ax = task_func(mu=0, sigma=1)
    bars = ax.patches
    assert len(bars) == 30, "There should be 30 bars in the histogram."

def test_task_func_fitted_curve():
    ax = task_func(mu=0, sigma=1)
    lines = ax.get_lines()
    assert lines[1].get_color() == 'g', "The fitted curve should be green."

def test_task_func_randomness():
    ax1 = task_func(mu=0, sigma=1, seed=0)
    ax2 = task_func(mu=0, sigma=1, seed=1)
    bars1 = [bar.get_height() for bar in ax1.patches]
    bars2 = [bar.get_height() for bar in ax2.patches]
    assert bars1 != bars2, "Different seeds should produce different histograms."

def test_task_func_model_fit():
    ax = task_func(mu=0, sigma=1)
    lines = ax.get_lines()
    fitted_line = lines[1]
    xdata, ydata = fitted_line.get_data()
    assert len(xdata) == 30 and len(ydata) == 30, "The fitted curve should have 30 points."