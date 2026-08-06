import pytest
from src_0594 import task_func
import os
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

@pytest.fixture
def temp_output_dir(tmpdir):
    return tmpdir.mkdir("test_output")

def test_task_func(temp_output_dir):
    hours = 2
    file_path, ax = task_func(hours, output_dir=str(temp_output_dir))

    # Check if the file exists
    assert os.path.exists(file_path)

    # Check if the file is not empty
    assert os.path.getsize(file_path) > 0

    # Read the CSV file
    df = pd.read_csv(file_path)

    # Check if the DataFrame is not empty
    assert not df.empty

    # Check if the DataFrame has the correct columns
    expected_columns = ['Time'] + ['Car', 'Bus', 'Truck', 'Bike']
    assert list(df.columns) == expected_columns

    # Check if the number of rows is correct (including the header)
    assert len(df) == hours + 1

    # Check if the plot axis is returned
    assert isinstance(ax, plt.Axes)

    # Clean up the generated files
    os.remove(file_path)