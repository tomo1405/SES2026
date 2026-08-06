import pytest
from src_0232 import task_func, ValueObject
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_with_empty_list():
    ax = task_func([])
    assert isinstance(ax, plt.Axes)
    assert ax.get_lines() == []  # No lines should be plotted for an empty list
    assert ax.get_patches() != []  # A single bar at 0 should be present

def test_task_func_with_single_value_object():
    obj = ValueObject(mu=5, std=2)
    ax = task_func([obj])
    assert isinstance(ax, plt.Axes)
    assert len(ax.get_lines()) == 1  # One line for the PDF
    assert len(ax.get_patches()) == 1  # One bar for the histogram

def test_task_func_with_multiple_value_objects():
    obj1 = ValueObject(mu=5, std=2)
    obj2 = ValueObject(mu=5, std=2)
    obj3 = ValueObject(mu=5, std=2)
    ax = task_func([obj1, obj2, obj3])
    assert isinstance(ax, plt.Axes)
    assert len(ax.get_lines()) == 1  # One line for the PDF
    assert len(ax.get_patches()) > 1  # Multiple bars for the histogram

def test_task_func_mean_and_std():
    obj1 = ValueObject(mu=5, std=2)
    obj2 = ValueObject(mu=5, std=2)
    obj3 = ValueObject(mu=5, std=2)
    ax = task_func([obj1, obj2, obj3])
    title = ax.get_title()
    mean, std = map(float, title.split('mu = ')[1].split(', std = '))
    assert np.isclose(mean, 5, atol=0.1)
    assert np.isclose(std, 2, atol=0.1)

def test_task_func_histogram_density():
    obj1 = ValueObject(mu=5, std=2)
    obj2 = ValueObject(mu=5, std=2)
    obj3 = ValueObject(mu=5, std=2)
    ax = task_func([obj1, obj2, obj3])
    hist_data = ax.patches[0].get_height()
    assert np.isclose(hist_data, 1/30, atol=0.01)  # Density should sum to 1 over the bins

def test_task_func_pdf_plot():
    obj1 = ValueObject(mu=5, std=2)
    obj2 = ValueObject(mu=5, std=2)
    obj3 = ValueObject(mu=5, std=2)
    ax = task_func([obj1, obj2, obj3])
    pdf_line = ax.get_lines()[0]
    x_data = pdf_line.get_xdata()
    y_data = pdf_line.get_ydata()
    assert np.allclose(y_data, stats.norm.pdf(x_data, 5, 2), atol=0.01)