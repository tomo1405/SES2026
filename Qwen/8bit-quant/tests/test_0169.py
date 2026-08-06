import pytest
from src_0169 import task_func
import pandas as pd
import numpy as np
import os

def test_task_func_default_labels():
    fig, data, plot_filename = task_func()
    
    # Check if the number of groups is correct
    assert len(data.columns) == 5
    
    # Check if the labels are correctly generated
    expected_labels = ['Group1', 'Group2', 'Group3', 'Group4', 'Group5']
    assert list(data.columns) == expected_labels
    
    # Check if the data size is correct
    assert len(data) == 5
    
    # Check if the plot file exists
    assert os.path.exists(plot_filename)
    
    # Clean up the plot file after test
    os.remove(plot_filename)

def test_task_func_custom_labels():
    custom_labels = ['A', 'B', 'C', 'D', 'E']
    fig, data, plot_filename = task_func(labels=custom_labels)
    
    # Check if the labels are correctly set
    assert list(data.columns) == custom_labels
    
    # Check if the plot file exists
    assert os.path.exists(plot_filename)
    
    # Clean up the plot file after test
    os.remove(plot_filename)

def test_task_func_custom_num_groups():
    fig, data, plot_filename = task_func(num_groups=3)
    
    # Check if the number of groups is correct
    assert len(data.columns) == 3
    
    # Check if the labels are correctly generated
    expected_labels = ['Group1', 'Group2', 'Group3']
    assert list(data.columns) == expected_labels
    
    # Check if the data size is correct
    assert len(data) == 5
    
    # Check if the plot file exists
    assert os.path.exists(plot_filename)
    
    # Clean up the plot file after test
    os.remove(plot_filename)

def test_task_func_custom_data_size():
    fig, data, plot_filename = task_func(data_size=10)
    
    # Check if the data size is correct
    assert len(data) == 10
    
    # Check if the plot file exists
    assert os.path.exists(plot_filename)
    
    # Clean up the plot file after test
    os.remove(plot_filename)