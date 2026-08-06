import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from src_0242 import task_func

def test_task_func():
    original = [(1, 2), (3, 4), (5, 6)]
    arr, norm_arr, ax = task_func(original)
    assert isinstance(arr, np.ndarray)
    assert isinstance(norm_arr, np.ndarray)
    assert isinstance(ax, plt.Axes)
    assert arr.size == len(original)
    assert norm_arr.size == len(original)
    assert ax.get_title() == "Original vs. Normalized Data"
    assert ax.get_legend().get_texts()[0].get_text() == "Original"
    assert ax.get_legend().get_texts()[1].get_text() == "Normalized"

def test_task_func_empty():
    original = []
    arr, norm_arr, ax = task_func(original)
    assert isinstance(arr, np.ndarray)
    assert isinstance(norm_arr, np.ndarray)
    assert isinstance(ax, plt.Axes)
    assert arr.size == 0
    assert norm_arr.size == 0
    assert ax.get_title() == "Original vs. Normalized Data"
    assert ax.get_legend() is None