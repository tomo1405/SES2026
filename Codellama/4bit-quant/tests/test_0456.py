import pytest
from src_0456 import task_func
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def test_task_func():
    # Test 1: Check if the function returns a numpy array
    samples = task_func(0, 1, 100)
    assert isinstance(samples, np.ndarray)

    # Test 2: Check if the function plots a histogram
    plt.figure(figsize=(10, 6))
    task_func(0, 1, 100)
    assert plt.gca().get_children()[0].__class__.__name__ == 'AxesImage'

    # Test 3: Check if the function plots a normal distribution
    plt.figure(figsize=(10, 6))
    task_func(0, 1, 100)
    assert plt.gca().get_children()[1].__class__.__name__ == 'Line2D'

    # Test 4: Check if the function sets the correct title
    plt.figure(figsize=(10, 6))
    task_func(0, 1, 100)
    assert plt.gca().get_children()[2].__class__.__name__ == 'Text'
    assert plt.gca().get_children()[2].get_text() == 'Normal Distribution: Mean = 0, Std Dev = 1'

    # Test 5: Check if the function sets the correct xlabel
    plt.figure(figsize=(10, 6))
    task_func(0, 1, 100)
    assert plt.gca().get_children()[3].__class__.__name__ == 'Text'
    assert plt.gca().get_children()[3].get_text() == 'Value'

    # Test 6: Check if the function sets the correct ylabel
    plt.figure(figsize=(10, 6))
    task_func(0, 1, 100)
    assert plt.gca().get_children()[4].__class__.__name__ == 'Text'
    assert plt.gca().get_children()[4].get_text() == 'Density'