import pytest
from src_0522 import task_func
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def test_task_func():
    # Sample data for testing
    data_list = [
        {'Test 1': 80, 'Test 2': 85, 'Test 3': 90},
        {'Test 1': 75, 'Test 2': 80, 'Test 3': 85},
        {'Test 1': 70, 'Test 2': 75, 'Test 3': 80}
    ]
    
    # Create a DataFrame from the sample data
    expected_df = pd.DataFrame(data_list)
    
    # Call the function
    ax = task_func(data_list)
    
    # Check if the DataFrame created inside the function matches the expected DataFrame
    actual_df = pd.DataFrame(ax.get_lines()[0].get_ydata(), columns=[ax.get_legend_handles_labels()[1][0]])
    for i, column in enumerate(expected_df.columns):
        assert all(expected_df[column] == actual_df.iloc[:, i])
    
    # Check if the plot has the correct title and labels
    assert ax.get_title() == "Student Scores over Tests"
    assert ax.get_xlabel() == "Test Number"
    assert ax.get_ylabel() == "Score"

    # Save the plot to a BytesIO object and encode it to base64 to check if the plot is generated correctly
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    encoded_plot = base64.b64encode(buf.getvalue()).decode('utf-8')
    
    # Assert that the encoded plot is not empty
    assert len(encoded_plot) > 0