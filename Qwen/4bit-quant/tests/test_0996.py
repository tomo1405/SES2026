import pytest
from src_0996 import task_func
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tempfile

# Mocking utilities
from unittest.mock import patch, mock_open

def test_task_func_file_not_found():
    with pytest.raises(FileNotFoundError):
        task_func("non_existent_file.csv", "plot.png")

def test_task_func_empty_file():
    with patch('src_0996.pd.read_csv', side_effect=pd.errors.EmptyDataError):
        result = task_func("empty_file.csv", "plot.png")
        assert result == (np.nan, np.nan, "plot.png")

def test_task_func_valid_data():
    # Prepare a temporary CSV file with valid data
    with tempfile.NamedTemporaryFile(delete=False, suffix='.csv') as temp_file:
        temp_file.write(b"1\n2\n3\n4\n5")
        temp_file.flush()
        temp_file_path = temp_file.name

    # Prepare a temporary file path for the plot
    with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_plot_file:
        temp_plot_path = temp_plot_file.name

    try:
        result = task_func(temp_file_path, temp_plot_path)
        mean, median, plot_path = result
        assert mean == 3.0
        assert median == 3.0
        assert plot_path == temp_plot_path

        # Check if the plot file was created
        assert os.path.exists(plot_path)

    finally:
        # Clean up temporary files
        os.remove(temp_file_path)
        os.remove(temp_plot_path)

def test_task_func_invalid_data():
    # Prepare a temporary CSV file with invalid data
    with tempfile.NamedTemporaryFile(delete=False, suffix='.csv') as temp_file:
        temp_file.write(b"a\nb\nc\n4\n5")
        temp_file.flush()
        temp_file_path = temp_file.name

    # Prepare a temporary file path for the plot
    with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_plot_file:
        temp_plot_path = temp_plot_file.name

    try:
        result = task_func(temp_file_path, temp_plot_path)
        mean, median, plot_path = result
        assert np.isnan(mean)
        assert np.isnan(median)
        assert plot_path == temp_plot_path

        # Check if the plot file was created
        assert os.path.exists(plot_path)

    finally:
        # Clean up temporary files
        os.remove(temp_file_path)
        os.remove(temp_plot_path)