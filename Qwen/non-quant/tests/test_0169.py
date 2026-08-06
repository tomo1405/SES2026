import pytest
from src_0169 import task_func
import pandas as pd
import matplotlib.pyplot as plt
import os

def test_task_func_default_labels():
    fig, data, plot_filename = task_func()
    
    # Check if the correct number of groups and data size is generated
    assert len(data.columns) == 5
    assert len(data) == 5
    
    # Check if default labels are generated correctly
    expected_labels = ['Group1', 'Group2', 'Group3', 'Group4', 'Group5']
    assert list(data.columns) == expected_labels
    
    # Check if the plot file is created
    assert os.path.exists(plot_filename)
    
    # Clean up the plot file after test
    os.remove(plot_filename)

def test_task_func_custom_labels():
    custom_labels = ['A', 'B', 'C', 'D', 'E']
    fig, data, plot_filename = task_func(labels=custom_labels)
    
    # Check if the correct number of groups and data size is generated
    assert len(data.columns) == 5
    assert len(data) == 5
    
    # Check if custom labels are applied correctly
    assert list(data.columns) == custom_labels
    
    # Check if the plot file is created
    assert os.path.exists(plot_filename)
    
    # Clean up the plot file after test
    os.remove(plot_filename)

def test_task_func_different_num_groups():
    fig, data, plot_filename = task_func(num_groups=3)
    
    # Check if the correct number of groups and data size is generated
    assert len(data.columns) == 3
    assert len(data) == 5
    
    # Check if default labels are generated correctly
    expected_labels = ['Group1', 'Group2', 'Group3']
    assert list(data.columns) == expected_labels
    
    # Check if the plot file is created
    assert os.path.exists(plot_filename)
    
    # Clean up the plot file after test
    os.remove(plot_filename)

def test_task_func_different_data_size():
    fig, data, plot_filename = task_func(data_size=10)
    
    # Check if the correct number of groups and data size is generated
    assert len(data.columns) == 5
    assert len(data) == 10
    
    # Check if default labels are generated correctly
    expected_labels = ['Group1', 'Group2', 'Group3', 'Group4', 'Group5']
    assert list(data.columns) == expected_labels
    
    # Check if the plot file is created
    assert os.path.exists(plot_filename)
    
    # Clean up the plot file after test
    os.remove(plot_filename)