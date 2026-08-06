import pytest
from src_0253 import task_func
import matplotlib.pyplot as plt
import numpy as np

def test_task_func():
    # Test with simple data and labels
    data = [np.arange(10), np.arange(10, 20)]
    labels = ['Series 1', 'Series 2']
    ax = task_func(data, labels)
    
    # Check if the plot has the correct number of lines
    assert len(ax.lines) == len(data)
    
    # Check if the labels are correctly set
    for line, label in zip(ax.lines, labels):
        assert line.get_label() == label
    
    # Check if the colors are correctly set
    expected_colors = ['red', 'green']
    for line, color in zip(ax.lines, expected_colors):
        assert line.get_color() == color
    
    # Check if the legend is present
    assert ax.get_legend() is not None

def test_task_func_with_more_data_than_colors():
    # Test with more data than colors available
    data = [np.arange(10), np.arange(10, 20), np.arange(20, 30)]
    labels = ['Series 1', 'Series 2', 'Series 3']
    ax = task_func(data, labels)
    
    # Check if the plot has the correct number of lines
    assert len(ax.lines) == len(data)
    
    # Check if the labels are correctly set
    for line, label in zip(ax.lines, labels):
        assert line.get_label() == label
    
    # Check if the colors are correctly set, with the last one being black
    expected_colors = ['red', 'green', 'blue', 'black']
    for line, color in zip(ax.lines, expected_colors):
        assert line.get_color() == color
    
    # Check if the legend is present
    assert ax.get_legend() is not None

def test_task_func_with_less_data_than_labels():
    # Test with less data than labels provided
    data = [np.arange(10)]
    labels = ['Series 1', 'Series 2']
    ax = task_func(data, labels)
    
    # Check if the plot has the correct number of lines
    assert len(ax.lines) == len(data)
    
    # Check if the labels are correctly set
    for line, label in zip(ax.lines, labels[:len(data)]):
        assert line.get_label() == label
    
    # Check if the colors are correctly set
    expected_colors = ['red']
    for line, color in zip(ax.lines, expected_colors):
        assert line.get_color() == color
    
    # Check if the legend is present
    assert ax.get_legend() is not None

def test_task_func_with_empty_data():
    # Test with empty data and labels
    data = []
    labels = []
    ax = task_func(data, labels)
    
    # Check if the plot has no lines
    assert len(ax.lines) == 0
    
    # Check if the legend is present
    assert ax.get_legend() is not None

def test_task_func_with_single_series():
    # Test with a single series
    data = [np.arange(10)]
    labels = ['Series 1']
    ax = task_func(data, labels)
    
    # Check if the plot has the correct number of lines
    assert len(ax.lines) == len(data)
    
    # Check if the label is correctly set
    assert ax.lines[0].get_label() == labels[0]
    
    # Check if the color is correctly set
    assert ax.lines[0].get_color() == 'red'
    
    # Check if the legend is present
    assert ax.get_legend() is not None