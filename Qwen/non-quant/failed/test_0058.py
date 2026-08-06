import pytest
from src_0058 import task_func
import pandas as pd
import io
import matplotlib.pyplot as plt

@pytest.fixture
def sample_csv():
    csv_data = io.StringIO(u"""A,B,C
1,2,3
4,5,6
7,8,9""")
    return csv_data

def test_task_func(sample_csv):
    # Mock the read_csv to return a sample DataFrame
    df = pd.read_csv(sample_csv)
    expected_corr = df.corr().round(2)
    
    # Call the function with a sample CSV and title
    corr, ax = task_func(sample_csv, "Sample Correlation Heatmap")
    
    # Check if the returned correlation matrix is as expected
    pd.testing.assert_frame_equal(corr, expected_corr)
    
    # Check if the plot title is set correctly
    assert ax.get_title() == "Sample Correlation Heatmap"
    
    # Check if the plot has the correct number of subplots
    assert len(ax.collections) > 0  # This checks if the heatmap was plotted

# To run the tests, use the following command in your terminal:
# pytest <path_to_this_file>