import pytest
from src_0556 import task_func
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

def test_task_func():
    a = np.array([1, 2, 3, 4, 5])
    b = np.array([2, 4, 6, 8, 10])
    correlation, ax = task_func(a, b)
    assert correlation == 1.0
    assert ax.get_xlabel() == 'A'
    assert ax.get_ylabel() == 'B'
    assert ax.get_title() == 'Correlation between A and B'
    assert len(ax.get_lines()) == 2
    assert ax.get_lines()[0].get_color() == 'red'
    assert ax.get_lines()[1].get_color() == 'blue'
    assert ax.get_lines()[0].get_label() == 'Regression line'
    assert ax.get_lines()[1].get_label() == 'Data points'
    assert ax.get_legend().get_title().get_text() == 'Legend'
    assert ax.get_legend().get_texts()[0].get_text() == 'Regression line'
    assert ax.get_legend().get_texts()[1].get_text() == 'Data points'