import pytest
from src_0253 import task_func
import matplotlib.pyplot as plt
import numpy as np

def test_task_func():
    # Prepare test data
    data = [
        np.array([1, 2, 3]),
        np.array([4, 5, 6]),
        np.array([7, 8, 9])
    ]
    labels = ['Series 1', 'Series 2', 'Series 3']
    
    # Call the function
    ax = task_func(data, labels)
    
    # Check if the plot has the correct number of lines
    assert len(ax.lines) == len(data)
    
    # Check if each line has the correct label and color
    for i, (line, label, expected_color) in enumerate(zip(ax.lines, labels, ['red', 'green', 'blue'])):
        assert line.get_label() == label
        assert line.get_color() == expected_color
    
    # Check if the legend is correctly set up
    legend_labels = [text.get_text() for text in ax.get_legend().get_texts()]
    assert legend_labels == labels

def test_task_func_with_less_data_than_colors():
    # Prepare test data with less series than colors
    data = [
        np.array([1, 2, 3]),
        np.array([4, 5, 6])
    ]
    labels = ['Series 1', 'Series 2']
    
    # Call the function
    ax = task_func(data, labels)
    
    # Check if the plot has the correct number of lines
    assert len(ax.lines) == len(data)
    
    # Check if each line has the correct label and color
    for i, (line, label, expected_color) in enumerate(zip(ax.lines, labels, ['red', 'green'])):
        assert line.get_label() == label
        assert line.get_color() == expected_color
    
    # Check if the legend is correctly set up
    legend_labels = [text.get_text() for text in ax.get_legend().get_texts()]
    assert legend_labels == labels

def test_task_func_with_more_data_than_colors():
    # Prepare test data with more series than colors
    data = [
        np.array([1, 2, 3]),
        np.array([4, 5, 6]),
        np.array([7, 8, 9]),
        np.array([10, 11, 12])
    ]
    labels = ['Series 1', 'Series 2', 'Series 3', 'Series 4']
    
    # Call the function
    ax = task_func(data, labels)
    
    # Check if the plot has the correct number of lines
    assert len(ax.lines) == len(data)
    
    # Check if each line has the correct label and color
    for i, (line, label, expected_color) in enumerate(zip(ax.lines, labels, ['red', 'green', 'blue', 'yellow'])):
        assert line.get_label() == label
        assert line.get_color() == expected_color
    
    # Check if the legend is correctly set up
    legend_labels = [text.get_text() for text in ax.get_legend().get_texts()]
    assert legend_labels == labels

def test_task_func_with_no_data():
    # Prepare test data with no series
    data = []
    labels = []
    
    # Call the function
    ax = task_func(data, labels)
    
    # Check if the plot has no lines
    assert len(ax.lines) == 0
    
    # Check if the legend is empty
    legend_labels = [text.get_text() for text in ax.get_legend().get_texts()]
    assert legend_labels == []

def test_task_func_with_single_series():
    # Prepare test data with a single series
    data = [np.array([1, 2, 3])]
    labels = ['Series 1']
    
    # Call the function
    ax = task_func(data, labels)
    
    # Check if the plot has one line
    assert len(ax.lines) == 1
    
    # Check if the line has the correct label and color
    line = ax.lines[0]
    assert line.get_label() == labels[0]
    assert line.get_color() == 'red'
    
    # Check if the legend is correctly set up
    legend_labels = [text.get_text() for text in ax.get_legend().get_texts()]
    assert legend_labels == labels