import pytest
from src_1055 import task_func
import os
import tempfile
import numpy as np

def create_temp_csv(data):
    with tempfile.NamedTemporaryFile(delete=False, mode='w', newline='') as temp_file:
        writer = csv.writer(temp_file)
        for value in data:
            writer.writerow([value])
    return temp_file.name

def test_task_func():
    # Create a temporary CSV file with known data
    data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    file_path = create_temp_csv(data)
    
    try:
        mean, std_dev, ax = task_func(file_path)
        
        # Check if the mean is calculated correctly
        expected_mean = np.mean(data[:30])  # Since we take 30 samples without replacement
        assert np.isclose(mean, expected_mean), f"Expected mean {expected_mean}, got {mean}"
        
        # Check if the standard deviation is calculated correctly
        expected_std_dev = np.std(data[:30], ddof=1)  # Since we take 30 samples without replacement
        assert np.isclose(std_dev, expected_std_dev), f"Expected std dev {expected_std_dev}, got {std_dev}"
        
        # Check if the plot has the correct title
        assert ax.get_title() == "Sample Histogram with Normal Distribution Overlay"
        
    finally:
        # Clean up the temporary file
        os.remove(file_path)

def test_task_func_io_error():
    # Test the case where the file does not exist
    with pytest.raises(IOError, match="Error reading the file. Please check the file path and permissions."):
        task_func("non_existent_file.csv")