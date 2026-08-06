import pytest
from src_0281 import task_func
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

def test_task_func_output():
    signal = np.array([1, 2, 3, 4, 5])
    expected_transformed_signal = np.round(fft(signal), 2).tolist()
    transformed_signal, ax = task_func(signal)
    
    assert np.array_equal(transformed_signal, expected_transformed_signal), "The transformed signal does not match the expected output."

def test_task_func_plot_titles():
    signal = np.array([1, 2, 3, 4, 5])
    _, ax = task_func(signal)
    
    assert ax[0].get_title() == 'Original Signal', "The first plot title is incorrect."
    assert ax[1].get_title() == 'Transformed Signal', "The second plot title is incorrect."

def test_task_func_plot_data():
    signal = np.array([1, 2, 3, 4, 5])
    _, ax = task_func(signal)
    
    assert np.array_equal(ax[0].lines[0].get_ydata(), signal), "The original signal data in the plot is incorrect."
    expected_transformed_signal = np.round(fft(signal), 2).tolist()
    assert np.array_equal(ax[1].lines[0].get_ydata(), expected_transformed_signal), "The transformed signal data in the plot is incorrect."

def test_task_func_random_seed():
    signal = np.array([1, 2, 3, 4, 5])
    transformed_signal_1, _ = task_func(signal, seed=777)
    transformed_signal_2, _ = task_func(signal, seed=777)
    
    assert np.array_equal(transformed_signal_1, transformed_signal_2), "The transformed signal is not reproducible with the same seed."

def test_task_func_precision():
    signal = np.array([1, 2, 3, 4, 5])
    transformed_signal, _ = task_func(signal, precision=3)
    
    expected_transformed_signal = np.round(fft(signal), 3).tolist()
    assert np.array_equal(transformed_signal, expected_transformed_signal), "The transformed signal does not match the expected output with the specified precision."

def test_task_func_return_type():
    signal = np.array([1, 2, 3, 4, 5])
    transformed_signal, ax = task_func(signal)
    
    assert isinstance(transformed_signal, np.ndarray), "The transformed signal should be a NumPy array."
    assert isinstance(ax, plt.AxesSubplot), "The returned axes object should be a matplotlib AxesSubplot instance."