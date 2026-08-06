import pytest
from src_0898 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_with_seed():
    rolls = 10
    seed = 42
    frequencies, ax = task_func(rolls, seed)
    
    # Check if the frequencies array has the correct length
    assert len(frequencies) == 6
    
    # Check if the sum of frequencies equals the number of rolls
    assert np.sum(frequencies) == rolls
    
    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes)

def test_task_func_without_seed():
    rolls = 10
    frequencies, ax = task_func(rolls)
    
    # Check if the frequencies array has the correct length
    assert len(frequencies) == 6
    
    # Check if the sum of frequencies equals the number of rolls
    assert np.sum(frequencies) == rolls
    
    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes)

def test_task_func_with_zero_rolls():
    rolls = 0
    frequencies, ax = task_func(rolls)
    
    # Check if the frequencies array has the correct length
    assert len(frequencies) == 6
    
    # Check if the sum of frequencies equals the number of rolls
    assert np.sum(frequencies) == rolls
    
    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes)

def test_task_func_with_large_rolls():
    rolls = 1000
    seed = 42
    frequencies, ax = task_func(rolls, seed)
    
    # Check if the frequencies array has the correct length
    assert len(frequencies) == 6
    
    # Check if the sum of frequencies equals the number of rolls
    assert np.sum(frequencies) == rolls
    
    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes)