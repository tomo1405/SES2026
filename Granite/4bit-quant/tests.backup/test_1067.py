import pytest
import numpy as np
import matplotlib.pyplot as plt
from src_1067 import task_func

NUM_SAMPLES = 100
NUM_OUTLIERS = 5

def test_task_func():
    data, outliers_detected, ax = task_func(num_samples=NUM_SAMPLES, num_outliers=NUM_OUTLIERS)
    assert isinstance(data, np.ndarray), "data should be a numpy array"
    assert isinstance(outliers_detected, np.ndarray), "outliers_detected should be a numpy array"
    assert isinstance(ax, plt.Axes), "ax should be a matplotlib Axes object"
    assert len(data) == NUM_SAMPLES + NUM_OUTLIERS, "data length should be equal to num_samples + num_outliers"
    assert len(outliers_detected) == NUM_OUTLIERS, "outliers_detected length should be equal to num_outliers"

def test_task_func_with_no_normal_data():
    data, outliers_detected, ax = task_func(num_samples=0, num_outliers=NUM_OUTLIERS)
    assert isinstance(data, np.ndarray), "data should be a numpy array"
    assert isinstance(outliers_detected, np.ndarray), "outliers_detected should be a numpy array"
    assert isinstance(ax, plt.Axes), "ax should be a matplotlib Axes object"
    assert len(data) == NUM_OUTLIERS, "data length should be equal to num_outliers"
    assert len(outliers_detected) == NUM_OUTLIERS, "outliers_detected length should be equal to num_outliers"