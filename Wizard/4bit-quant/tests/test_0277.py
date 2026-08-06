python
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import pytest

def task_func(matrix):
    max_values = [max(row) for row in matrix]
    
    fig, ax = plt.subplots()
    ax.hist(max_values, bins=10, density=True, alpha=0.6, color='g')
    
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, np.mean(max_values), np.std(max_values))
    ax.plot(x, p, 'k', linewidth=2)

    skewness = stats.skew(max_values)
    kurtosis = stats.kurtosis(max_values)

    return skewness, kurtosis, ax

def test_task_func():
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    skewness, kurtosis, ax = task_func(matrix)
    assert skewness == pytest.approx(0.0, abs=1e-2)
    assert kurtosis == pytest.approx(0.0, abs=1e-2)
    assert ax is not None