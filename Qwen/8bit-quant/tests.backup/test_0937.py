import pytest
from src_0937 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_valid_input():
    word = "hello"
    ax = task_func(word)
    
    # Check if the correct number of bars are plotted
    assert len(ax.patches) == len(word)
    
    # Check if the bar heights correspond to the correct alphabetical positions
    expected_positions = np.array([8, 5, 12, 12, 15])
    actual_positions = np.array([patch.get_height() for patch in ax.patches])
    assert np.array_equal(actual_positions, expected_positions)
    
    # Check plot labels and title
    assert ax.get_xlabel() == 'Letter Index'
    assert ax.get_ylabel() == 'Alphabetical Position'
    assert ax.get_title() == 'Alphabetical Position of Letters in Word'

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func("Hello123")

def test_task_func_single_letter():
    word = "a"
    ax = task_func(word)
    
    # Check if the correct number of bars are plotted
    assert len(ax.patches) == len(word)
    
    # Check if the bar height corresponds to the correct alphabetical position
    expected_position = np.array([1])
    actual_position = np.array([patch.get_height() for patch in ax.patches])
    assert np.array_equal(actual_position, expected_position)
    
    # Check plot labels and title
    assert ax.get_xlabel() == 'Letter Index'
    assert ax.get_ylabel() == 'Alphabetical Position'
    assert ax.get_title() == 'Alphabetical Position of Letters in Word'