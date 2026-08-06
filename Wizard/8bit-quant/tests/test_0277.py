python
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
from src_0277 import task_func

def test_task_func():
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    skewness, kurtosis, ax = task_func(matrix)
    assert skewness == 0
    assert kurtosis == 0
    assert ax.get_title() == 'Histogram of maximum values'
    assert ax.get_xlabel() == 'Maximum value'
    assert ax.get_ylabel() == 'Density'
    assert ax.get_xlim() == (-2.5, 9.5)
    assert ax.get_ylim() == (0, 0.4)
    assert ax.get_xticks() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert ax.get_yticks() == [0, 0.1, 0.2, 0.3, 0.4]
    assert ax.get_legend().get_texts()[0].get_text() == 'Gaussian distribution'
    assert ax.get_legend().get_texts()[1].get_text() == 'Histogram of maximum values'