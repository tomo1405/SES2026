import io
import sys

import pytest
from src_0163 import task_func


# Mocking the plot to capture it for testing
@pytest.mark.mpl_image_compare(style='default', tolerance=20)
def test_task_func():
    # Redirect stdout to capture any print statements (if any)
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    # Call the function with a sample text
    ax = task_func("Hello, world! This is a test.")
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    # Return the Axes object for comparison
    return ax

def test_task_func_no_words():
    # Test with a string that contains no words
    ax = task_func("!!! ### $$$")
    
    # Check if the bins are set to an empty list
    assert ax.collections[0].get_offsets().size == 0

def test_task_func_empty_string():
    # Test with an empty string
    ax = task_func("")
    
    # Check if the bins are set to an empty list
    assert ax.collections[0].get_offsets().size == 0

def test_task_func_single_word():
    # Test with a single word
    ax = task_func("Python")
    
    # Check if the histogram has one bar with height 1
    assert len(ax.patches) == 1
    assert ax.patches[0].get_height() == 1

def test_task_func_rwidth():
    # Test with a custom rwidth value
    ax = task_func("This is a test.", rwidth=0.5)
    
    # Check if the rwidth is set correctly
    assert ax.patches[0].get_width() == 0.5 * (ax.patches[0].get_x1() - ax.patches[0].get_x0())