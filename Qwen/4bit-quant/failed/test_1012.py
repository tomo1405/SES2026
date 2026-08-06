import pytest
from src_1012 import task_func
import pandas as pd
import io
import matplotlib.pyplot as plt

@pytest.fixture
def sample_csv():
    data = io.StringIO("column1,column2\nA,10\nA,20\nB,30\nB,40")
    return data

def test_task_func(sample_csv):
    # Mock the reading of CSV file
    expected_df = pd.read_csv(sample_csv)
    expected_groupby_data = expected_df.groupby('column1')['column2'].mean()

    # Capture the plot output
    fig, ax = plt.subplots()
    task_func(sample_csv, col1_name='column1', col2_name='column2')

    # Check if the plot has the correct title and labels
    assert ax.get_title() == "Mean of column2 Grouped by column1"
    assert ax.get_xlabel() == "column1"
    assert ax.get_ylabel() == "Mean of column2"

    # Check if the plot data matches the expected groupby data
    bars = ax.patches
    for i, bar in enumerate(bars):
        assert bar.get_height() == expected_groupby_data[i]

    # Clean up the plot
    plt.close(fig)