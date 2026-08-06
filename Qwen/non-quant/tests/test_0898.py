import pytest
from src_0898 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_output():
    rolls = 10
    seed = 42
    expected_frequencies = np.array([1, 2, 3, 1, 1, 2])  # Example expected output for 10 rolls with seed 42
    frequencies, ax = task_func(rolls, seed)
    
    assert np.array_equal(frequencies, expected_frequencies), f"Expected {expected_frequencies}, but got {frequencies}"

def test_task_func_seed_consistency():
    rolls = 10
    seed = 42
    frequencies1, _ = task_func(rolls, seed)
    frequencies2, _ = task_func(rolls, seed)
    
    assert np.array_equal(frequencies1, frequencies2), "Frequencies do not match for the same seed"

def test_task_func_no_seed():
    rolls = 10
    frequencies1, _ = task_func(rolls)
    frequencies2, _ = task_func(rolls)
    
    assert not np.array_equal(frequencies1, frequencies2), "Frequencies should differ without a seed"

def test_task_func_histogram_properties():
    rolls = 10
    _, ax = task_func(rolls)
    
    assert isinstance(ax, plt.Axes), "The returned object is not a matplotlib Axes"
    assert ax.get_title() == 'Histogram of Dice Rolls', "Title of the histogram is incorrect"
    assert ax.get_xlabel() == 'Dice Value', "X-axis label is incorrect"
    assert ax.get_ylabel() == 'Frequency', "Y-axis label is incorrect"

def test_task_func_bincount_length():
    rolls = 10
    frequencies, _ = task_func(rolls)
    
    assert len(frequencies) == 6, "Length of frequencies array should be 6 (for dice values 1 to 6)"