import pytest
from src_0062 import task_func
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

def test_task_func_with_valid_data():
    # Sample input data
    result = [
        {'from_user': 4},
        {'from_user': 9},
        {'from_user': 16}
    ]
    
    # Expected output
    expected_square_roots = np.array([2.0, 3.0, 4.0])
    
    # Call the function
    square_roots, ax = task_func(result)
    
    # Check if the calculated square roots are correct
    assert np.allclose(square_roots, expected_square_roots), f"Expected {expected_square_roots}, got {square_roots}"
    
    # Check if the plot has the correct title, x-label, and y-label
    assert ax.get_title() == 'Square root plot'
    assert ax.get_xlabel() == 'x'
    assert ax.get_ylabel() == 'sqrt(x)'
    
    # Check if the annotation is present and correctly formatted
    annotations = ax.texts
    assert len(annotations) == 1, "There should be exactly one annotation"
    now_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    assert annotations[0].get_text().startswith(now_str[:10]), "Annotation should contain the current date"

def test_task_func_with_no_from_user():
    # Sample input data without 'from_user' key
    result = [
        {'other_key': 4},
        {'other_key': 9},
        {'other_key': 16}
    ]
    
    # Expected output
    expected_square_roots = np.array([])
    
    # Call the function
    square_roots, ax = task_func(result)
    
    # Check if the calculated square roots are correct
    assert np.allclose(square_roots, expected_square_roots), f"Expected {expected_square_roots}, got {square_roots}"
    
    # Check if the plot has no data points
    assert len(ax.lines[0].get_xdata()) == 0, "Plot should have no data points"

def test_task_func_with_empty_list():
    # Sample input data as an empty list
    result = []
    
    # Expected output
    expected_square_roots = np.array([])
    
    # Call the function
    square_roots, ax = task_func(result)
    
    # Check if the calculated square roots are correct
    assert np.allclose(square_roots, expected_square_roots), f"Expected {expected_square_roots}, got {square_roots}"
    
    # Check if the plot has no data points
    assert len(ax.lines[0].get_xdata()) == 0, "Plot should have no data points"