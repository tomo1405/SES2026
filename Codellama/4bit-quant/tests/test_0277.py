import pytest
from src_0277 import task_func
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def test_task_func():
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    skewness, kurtosis, ax = task_func(matrix)
    assert skewness == 0
    assert kurtosis == 3
    assert ax.get_title() == 'Histogram of Maximum Values'
    assert ax.get_xlabel() == 'Maximum Values'
    assert ax.get_ylabel() == 'Frequency'
    assert ax.get_xlim() == (0, 9)
    assert ax.get_ylim() == (0, 3)
    assert ax.get_yticks() == np.linspace(0, 3, 4)
    assert ax.get_xticks() == np.linspace(0, 9, 10)
    assert ax.get_xticklabels() == ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    assert ax.get_yticklabels() == ['0', '1', '2', '3']
    assert ax.get_lines()[0].get_xdata() == np.linspace(0, 9, 100)
    assert ax.get_lines()[0].get_ydata() == stats.norm.pdf(np.linspace(0, 9, 100), np.mean(max_values), np.std(max_values))
    assert ax.get_lines()[0].get_color() == 'k'
    assert ax.get_lines()[0].get_linewidth() == 2