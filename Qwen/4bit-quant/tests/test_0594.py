import pytest
from src_0594 import task_func
import os
import pandas as pd

def test_task_func(tmpdir):
    # Create a temporary directory for output
    output_dir = tmpdir.mkdir("output")

    # Call the function with 1 hour of data
    file_path, ax = task_func(1, str(output_dir))

    # Check if the file was created
    assert os.path.exists(file_path)

    # Read the CSV file
    df = pd.read_csv(file_path)

    # Check if the DataFrame is not empty
    assert not df.empty

    # Check if the DataFrame has the correct columns
    assert all(column in df.columns for column in ['Time'] + ['Car', 'Bus', 'Truck', 'Bike'])

    # Check if the number of rows is correct (including the header row)
    assert len(df) == 2  # 1 header row + 1 data row

    # Check if the plot object is returned (this is a basic check)
    assert isinstance(ax, plt.Axes)

    # Clean up the temporary directory
    os.remove(file_path)