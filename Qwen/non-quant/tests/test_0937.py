import pytest
from src_0937 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_valid_input():
    # Test with a valid input word
    word = "hello"
    ax = task_func(word)
    
    # Check if the axis object is created
    assert isinstance(ax, plt.Axes)
    
    # Check if the bar chart data is correct
    expected_positions = np.array([8, 5, 12, 12, 15])
    actual_positions = ax.containers[0].datavalues
    assert np.array_equal(actual_positions, expected_positions)

def test_task_func_invalid_input():
    # Test with an invalid input word containing non-alphabetic characters
    word = "hello123"
    with pytest.raises(ValueError) as excinfo:
        task_func(word)
    assert str(excinfo.value) == "The word should contain only lowercase alphabetic characters."

def test_task_func_single_letter():
    # Test with a single letter input
    word = "a"
    ax = task_func(word)
    
    # Check if the axis object is created
    assert isinstance(ax, plt.Axes)
    
    # Check if the bar chart data is correct
    expected_positions = np.array([1])
    actual_positions = ax.containers[0].datavalues
    assert np.array_equal(actual_positions, expected_positions)

def test_task_func_empty_string():
    # Test with an empty string input
    word = ""
    with pytest.raises(ValueError) as excinfo:
        task_func(word)
    assert str(excinfo.value) == "The word should contain only lowercase alphabetic characters."