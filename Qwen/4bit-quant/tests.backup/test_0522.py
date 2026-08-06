import pytest
from src_0522 import task_func
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def test_task_func():
    # Create a sample data list
    data_list = [
        [85, 90, 78],
        [92, 88, 91],
        [79, 82, 84]
    ]
    
    # Call the function
    ax = task_func(data_list)
    
    # Check if the plot is created with the correct title and labels
    assert ax.get_title() == "Student Scores over Tests"
    assert ax.get_xlabel() == "Test Number"
    assert ax.get_ylabel() == "Score"
    
    # Check if the plot contains the correct number of lines
    assert len(ax.get_lines()) == len(data_list)
    
    # Check if the plot contains the correct labels
    labels = [line.get_label() for line in ax.get_lines()]
    assert labels == ['0', '1', '2']

# Helper function to convert plot to image and compare
def plot_to_base64(plot):
    buf = BytesIO()
    plot.figure.savefig(buf, format='png')
    buf.seek(0)
    img_str = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()
    return img_str

# Test to ensure the plot content is as expected
def test_plot_content():
    data_list = [
        [85, 90, 78],
        [92, 88, 91],
        [79, 82, 84]
    ]
    
    ax = task_func(data_list)
    
    # Convert the plot to base64
    plot_image = plot_to_base64(ax)
    
    # Expected base64 string (this should be replaced with the actual expected base64 string)
    expected_image = "expected_base64_string_here"
    
    # Compare the actual and expected images
    assert plot_image == expected_image, "The plot does not match the expected output."