import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from src_0277 import task_func

def test_task_func():
    matrix = np.random.rand(100, 100)
    skewness, kurtosis, ax = task_func(matrix)
    assert isinstance(skewness, float)
    assert isinstance(kurtosis, float)
    assert isinstance(ax, plt.Axes)

def test_task_func_with_zero_matrix():
    matrix = np.zeros((100, 100))
    skewness, kurtosis, ax = task_func(matrix)
    assert skewness == 0
    assert kurtosis == 3

def test_task_func_with_identity_matrix():
    matrix = np.eye(100)
    skewness, kurtosis, ax = task_func(matrix)
    assert skewness == 0
    assert kurtosis == 1.2