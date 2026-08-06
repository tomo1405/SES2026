import pytest
from src_0541 import task_func
import matplotlib.pyplot as plt
import numpy as np

def test_task_func():
    # Prepare test data
    list_of_menuitems = [['burger', 'fries'], ['burger', 'soda'], ['fries', 'soda']]
    
    # Call the function
    ax = task_func(list_of_menuitems)
    
    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes), "The function should return a matplotlib Axes object"
    
    # Check if the plot has the correct number of bars
    bars = ax.patches
    assert len(bars) == 3, "There should be 3 bars in the plot (one for each unique menu item)"
    
    # Check if the plot has the correct labels
    labels = [label.get_text() for label in ax.get_xticklabels()]
    assert set(labels) == {'burger', 'fries', 'soda'}, "The plot should have 'burger', 'fries', and 'soda' as labels"
    
    # Check if the plot has the correct title
    assert ax.get_title() == "Menu Distribution", "The plot should have the title 'Menu Distribution'"
    
    # Check if the plot has the correct x and y labels
    assert ax.get_xlabel() == "Menu Items", "The x-axis should be labeled 'Menu Items'"
    assert ax.get_ylabel() == "Frequency", "The y-axis should be labeled 'Frequency'"
    
    # Check if the plot has the correct colors
    colors = [bar.get_facecolor() for bar in bars]
    assert all(color == (0.0, 0.0, 1.0, 1.0) for color in colors), "All bars should have the color blue (default)"

# To run the tests, use the command: pytest <filename>.py