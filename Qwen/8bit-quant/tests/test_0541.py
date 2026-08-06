import pytest
from src_0541 import task_func
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_basic():
    # Test with a simple list of menu items
    list_of_menuitems = [['burger', 'fries'], ['burger', 'soda']]
    ax = task_func(list_of_menuitems)
    
    # Check that the plot has the correct number of bars
    assert len(ax.patches) == 3  # 'burger', 'fries', 'soda'

    # Check that the labels and values are correct
    labels = [patch.get_label() for patch in ax.patches]
    expected_labels = ['burger', 'fries', 'soda']
    assert labels == expected_labels

    values = [patch.get_height() for patch in ax.patches]
    expected_values = [2, 1, 1]  # 'burger' appears twice, 'fries' and 'soda' once
    assert values == expected_values

def test_task_func_with_custom_title_and_color():
    # Test with custom title and color
    list_of_menuitems = [['pizza', 'pasta'], ['pizza', 'salad']]
    ax = task_func(list_of_menuitems, title="Custom Title", color="green")
    
    # Check that the title and color are set correctly
    assert ax.get_title() == "Custom Title"
    assert all(patch.get_facecolor() == (0, 1, 0, 1) for patch in ax.patches)  # Green color

def test_task_func_with_empty_list():
    # Test with an empty list of menu items
    list_of_menuitems = []
    ax = task_func(list_of_menuitems)
    
    # Check that there are no bars in the plot
    assert len(ax.patches) == 0

def test_task_func_with_single_item():
    # Test with a single menu item
    list_of_menuitems = [['soup']]
    ax = task_func(list_of_menuitems)
    
    # Check that there is one bar in the plot
    assert len(ax.patches) == 1
    assert ax.patches[0].get_label() == 'soup'
    assert ax.patches[0].get_height() == 1

def test_task_func_with_multiple_items():
    # Test with multiple menu items
    list_of_menuitems = [['apple', 'banana'], ['banana', 'cherry'], ['apple', 'cherry']]
    ax = task_func(list_of_menuitems)
    
    # Check that the plot has the correct number of bars
    assert len(ax.patches) == 3  # 'apple', 'banana', 'cherry'

    # Check that the labels and values are correct
    labels = [patch.get_label() for patch in ax.patches]
    expected_labels = ['apple', 'banana', 'cherry']
    assert labels == expected_labels

    values = [patch.get_height() for patch in ax.patches]
    expected_values = [2, 2, 2]  # Each item appears twice
    assert values == expected_values