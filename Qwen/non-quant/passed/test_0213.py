import pytest
from src_0213 import task_func
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    return [(1, 2), (3, 4), (5, 6)]

def test_task_func(sample_data):
    ax, max_y_point = task_func(sample_data)
    
    # Check if the max_y_point is correctly identified
    assert max_y_point == (5, 6)
    
    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes)
    assert len(ax.collections) == 2  # One scatter plot for all points, one for the max point
    
    # Check if the labels and title are set correctly
    assert ax.get_xlabel() == 'x'
    assert ax.get_ylabel() == 'y'
    assert ax.get_title() == 'Points with Max Y Point Highlighted'
    
    # Check if the legend is present
    assert ax.get_legend() is not None

def test_task_func_with_single_point():
    data = [(1, 2)]
    ax, max_y_point = task_func(data)
    
    # Check if the max_y_point is correctly identified
    assert max_y_point == (1, 2)
    
    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes)
    assert len(ax.collections) == 2  # One scatter plot for all points, one for the max point
    
    # Check if the labels and title are set correctly
    assert ax.get_xlabel() == 'x'
    assert ax.get_ylabel() == 'y'
    assert ax.get_title() == 'Points with Max Y Point Highlighted'
    
    # Check if the legend is present
    assert ax.get_legend() is not None

def test_task_func_with_identical_points():
    data = [(1, 2), (1, 2), (1, 2)]
    ax, max_y_point = task_func(data)
    
    # Check if the max_y_point is correctly identified
    assert max_y_point == (1, 2)
    
    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes)
    assert len(ax.collections) == 2  # One scatter plot for all points, one for the max point
    
    # Check if the labels and title are set correctly
    assert ax.get_xlabel() == 'x'
    assert ax.get_ylabel() == 'y'
    assert ax.get_title() == 'Points with Max Y Point Highlighted'
    
    # Check if the legend is present
    assert ax.get_legend() is not None