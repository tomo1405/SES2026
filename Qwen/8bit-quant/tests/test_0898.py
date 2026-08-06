import pytest
from src_0898 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_with_seed():
    rolls = 10
    seed = 42
    expected_frequencies = np.array([2, 1, 1, 1, 3, 2])
    
    frequencies, ax = task_func(rolls, seed)
    
    assert np.array_equal(frequencies, expected_frequencies), f"Expected {expected_frequencies}, but got {frequencies}"
    assert isinstance(ax, plt.Axes), "Return value should be a tuple with a matplotlib Axes object"

def test_task_func_without_seed():
    rolls = 10
    frequencies, ax = task_func(rolls)
    
    assert len(frequencies) == 6, "Frequencies array should have 6 elements"
    assert isinstance(ax, plt.Axes), "Return value should be a tuple with a matplotlib Axes object"

def test_task_func_zero_rolls():
    rolls = 0
    frequencies, ax = task_func(rolls)
    
    assert np.array_equal(frequencies, np.zeros(6)), "Frequencies should be all zeros for zero rolls"
    assert isinstance(ax, plt.Axes), "Return value should be a tuple with a matplotlib Axes object"

def test_task_func_large_rolls():
    rolls = 1000
    seed = 42
    expected_frequencies = np.array([165, 168, 171, 166, 171, 169])
    
    frequencies, ax = task_func(rolls, seed)
    
    assert np.allclose(frequencies, expected_frequencies, atol=10), "Frequencies should be close to expected values"
    assert isinstance(ax, plt.Axes), "Return value should be a tuple with a matplotlib Axes object"