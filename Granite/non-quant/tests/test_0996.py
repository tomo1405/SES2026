import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from unittest.mock import patch
from io import StringIO

def task_func(file_path: str, plot_path: str) -> (float, float, str):
    # Check if file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File {file_path} does not exist.")

    # Load data and handle empty file
    try:
        data = pd.read_csv(file_path)
    except pd.errors.EmptyDataError:
        return np.nan, np.nan, plot_path

    # Convert data to numeric, coerce errors to NaN
    data = pd.to_numeric(data.squeeze(), errors="coerce")

    # Ensure data is a Pandas Series
    if not isinstance(data, pd.Series):
        data = pd.Series(data)

    # Clean data
    data = data.dropna()

    # Perform analysis
    if data.empty:
        mean = median = np.nan
    else:
        # Calculate mean and median
        mean = float(np.mean(data))
        median = float(np.median(data))

    # Create plot and save it
    plt.figure(figsize=(10, 6))
    plt.plot(data)
    plt.title("Data Visualization")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.savefig(plot_path)
    plt.close()

    return mean, median, plot_path

def test_task_func():
    with patch("src_0996.plt.savefig") as mock_savefig:
        with patch("src_0996.pd.read_csv", return_value=pd.Series([1, 2, 3])) as mock_read_csv:
            mean, median, plot_path = task_func("test_file.csv", "test_plot.png")
            mock_read_csv.assert_called_once_with("test_file.csv")
            assert mean == 2
            assert median == 2
            mock_savefig.assert_called_once()

def test_task_func_file_not_found():
    with patch("src_0996.plt.savefig") as mock_savefig:
        with patch("src_0996.os.path.isfile", return_value=False) as mock_isfile:
            with patch("src_0996.pd.read_csv") as mock_read_csv:
                try:
                    task_func("test_file.csv", "test_plot.png")
                except FileNotFoundError as e:
                    assert str(e) == "File test_file.csv does not exist."
                else:
                    assert False, "Expected FileNotFoundError was not raised."
                mock_isfile.assert_called_once_with("test_file.csv")
                mock_read_csv.assert_not_called()
                mock_savefig.assert_not_called()

def test_task_func_empty_file():
    with patch("src_0996.plt.savefig") as mock_savefig:
        with patch("src_0996.os.path.isfile", return_value=True) as mock_isfile:
            with patch("src_0996.pd.read_csv", side_effect=pd.errors.EmptyDataError) as mock_read_csv:
                mean, median, plot_path = task_func("test_file.csv", "test_plot.png")
                mock_isfile.assert_called_once_with("test_file.csv")
                mock_read_csv.assert_called_once_with("test_file.csv")
                assert mean is np.nan
                assert median is np.nan
                mock_savefig.assert_called_once()

def test_task_func_non_numeric_data():
    with patch("src_0996.plt.savefig") as mock_savefig:
        with patch("src_0996.os.path.isfile", return_value=True) as mock_isfile:
            with patch("src_0996.pd.read_csv", return_value=pd.Series(["a", "b", "c"])) as mock_read_csv:
                mean, median, plot_path = task_func("test_file.csv", "test_plot.png")
                mock_isfile.assert_called_once_with("test_file.csv")
                mock_read_csv.assert_called_once_with("test_file.csv")
                assert mean == 2
                assert median == 2
                mock_savefig.assert_called_once()