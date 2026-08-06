import pytest
from src_0594 import task_func
import os
import pandas as pd
from datetime import datetime

# Constants
VEHICLE_TYPES = ['Car', 'Bus', 'Truck', 'Bike']
OUTPUT_DIR = './output'

def test_task_func():
    # Ensure the output directory exists
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Call the function
    file_path, ax = task_func(1, OUTPUT_DIR)

    # Check if the file path is correct
    assert file_path == os.path.join(OUTPUT_DIR, 'traffic_data.csv')

    # Check if the file exists
    assert os.path.exists(file_path)

    # Read the CSV file
    df = pd.read_csv(file_path)

    # Check if the DataFrame is not empty
    assert not df.empty

    # Check if the DataFrame has the correct columns
    expected_columns = ['Time'] + VEHICLE_TYPES
    assert list(df.columns) == expected_columns

    # Check if the DataFrame has the correct number of rows (including header)
    assert len(df) == 2  # 1 header row + 1 data row

    # Check if the first row contains the correct time format
    first_time = df.iloc[0]['Time']
    assert isinstance(first_time, str)
    assert datetime.strptime(first_time, '%Y-%m-%d %H:%M:%S.%f')

    # Check if the vehicle counts are within the expected range
    for vehicle_type in VEHICLE_TYPES:
        count = df.iloc[0][vehicle_type]
        assert 0 <= count <= 50

    # Since we cannot check the plot directly, we assume it is generated correctly
    # if the function reaches this point without errors.

    # Clean up the created file
    os.remove(file_path)