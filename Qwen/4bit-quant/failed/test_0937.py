import pytest
from src_0937 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_valid_input():
    # Test with a valid input
    result = task_func("hello")
    assert isinstance(result, plt.Axes)
    # Check if the plot is correctly configured
    assert result.get_xlabel() == 'Letter Index'
    assert result.get_ylabel() == 'Alphabetical Position'
    assert result.get_title() == 'Alphabetical Position of Letters in Word'

def test_task_func_invalid_input():
    # Test with an invalid input
    with pytest.raises(ValueError, match="The word should contain only lowercase alphabetic characters."):
        task_func("Hello")

def test_task_func_single_letter():
    # Test with a single letter
    result = task_func("a")
    assert isinstance(result, plt.Axes)
    # Check if the plot is correctly configured
    assert result.get_xlabel() == 'Letter Index'
    assert result.get_ylabel() == 'Alphabetical Position'
    assert result.get_title() == 'Alphabetical Position of Letters in Word'

def test_task_func_multiple_same_letters():
    # Test with multiple same letters
    result = task_func("aaa")
    assert isinstance(result, plt.Axes)
    # Check if the plot is correctly configured
    assert result.get_xlabel() == 'Letter Index'
    assert result.get_ylabel() == 'Alphabetical Position'
    assert result.get_title() == 'Alphabetical Position of Letters in Word'

def test_task_func_empty_string():
    # Test with an empty string
    with pytest.raises(ValueError, match="The word should contain only lowercase alphabetic characters."):
        task_func("")