import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from unittest.mock import patch

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
    with patch("matplotlib.pyplot.savefig") as mock_savefig:
        file_path = "test_file.csv"
        plot_path = "test_plot.png"
        mean, median, plot_path = task_func(file_path, plot_path)
        assert isinstance(mean, float) or np.isnan(mean)
        assert isinstance(median, float) or np.isnan(median)
        assert plot_path == "test_plot.png"
        mock_savefig.assert_called_once()

def test_task_func_file_not_found():
    file_path = "nonexistent_file.csv"
    plot_path = "test_plot.png"
    with patch("os.path.isfile", return_value=False):
        with patch("matplotlib.pyplot.savefig") as mock_savefig:
            mean, median, plot_path = task_func(file_path, plot_path)
            assert np.isnan(mean)
            assert np.isnan(median)
            assert plot_path == "test_plot.png"
            mock_savefig.assert_not_called()

def test_task_func_empty_file():
    file_path = "empty_file.csv"
    plot_path = "test_plot.png"
    with patch("pandas.read_csv", side_effect=pd.errors.EmptyDataError):
        with patch("matplotlib.pyplot.savefig") as mock_savefig:
            mean, median, plot_path = task_func(file_path, plot_path)
            assert np.isnan(mean)
            assert np.isnan(median)
            assert plot_path == "test_plot.png"
            mock_savefig.assert_called_once()

def test_task_func_data_type_error():
    file_path = "invalid_data_type.csv"
    plot_path = "test_plot.png"
    with patch("pandas.to_numeric", side_effect=pd.errors.ParserError):
        with patch("matplotlib.pyplot.savefig") as mock_savefig:
            mean, median, plot_path = task_func(file_path, plot_path)
            assert np.isnan(mean)
            assert np.isnan(median)
            assert plot_path == "test_plot.png"
            mock_savefig.assert_called_once()

def test_task_func_data_not_series():
    file_path = "not_series.csv"
    plot_path = "test_plot.png"
    with patch("pandas.Series", return_value=123):
        with patch("matplotlib.pyplot.savefig") as mock_savefig:
            mean, median, plot_path = task_func(file_path, plot_path)
            assert mean == 123
            assert median == 123
            assert plot_path == "test_plot.png"
            mock_savefig.assert_called_once()

def test_task_func_data_cleaning():
    file_path = "dirty_data.csv"
    plot_path = "test_plot.png"
    data = pd.Series([1, 2, np.nan, 4, 5])
    with patch("pandas.read_csv", return_value=data):
        with patch("matplotlib.pyplot.savefig") as mock_savefig:
            mean, median, plot_path = task_func(file_path, plot_path)
            assert mean == 3
            assert median == 3
            assert plot_path == "test_plot.png"
            mock_savefig.assert_called_once()