python
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pytest

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
    # Test case 1: Valid file path, valid plot path
    file_path = "data.csv"
    plot_path = "plot.png"
    mean, median, plot_path = task_func(file_path, plot_path)
    assert mean == 1.23
    assert median == 4.56
    assert os.path.isfile(plot_path)

    # Test case 2: Invalid file path, valid plot path
    file_path = "invalid_file.csv"
    plot_path = "plot.png"
    with pytest.raises(FileNotFoundError):
        task_func(file_path, plot_path)

    # Test case 3: Valid file path, invalid plot path
    file_path = "data.csv"
    plot_path = "invalid_plot.png"
    with pytest.raises(FileNotFoundError):
        task_func(file_path, plot_path)

    # Test case 4: Empty file, valid plot path
    file_path = "empty_file.csv"
    plot_path = "plot.png"
    with open(file_path, "w") as f:
        f.write("")
    mean, median, plot_path = task_func(file_path, plot_path)
    assert np.isnan(mean)
    assert np.isnan(median)
    assert os.path.isfile(plot_path)

    # Test case 5: Valid file path, valid plot path, no data
    file_path = "no_data.csv"
    plot_path = "plot.png"
    with open(file_path, "w") as f:
        f.write("col1,col2\n")
    mean, median, plot_path = task_func(file_path, plot_path)
    assert np.isnan(mean)
    assert np.isnan(median)
    assert os.path.isfile(plot_path)

    # Test case 6: Valid file path, valid plot path, all NaN data
    file_path = "all_nan_data.csv"
    plot_path = "plot.png"
    with open(file_path, "w") as f:
        f.write("col1,col2\nNaN,NaN")
    mean, median, plot_path = task_func(file_path, plot_path)
    assert np.isnan(mean)
    assert np.isnan(median)
    assert os.path.isfile(plot_path)

    # Test case 7: Valid file path, valid plot path, all zero data
    file_path = "all_zero_data.csv"
    plot_path = "plot.png"
    with open(file_path, "w") as f:
        f.write("col1,col2\n0,0")
    mean, median, plot_path = task_func(file_path, plot_path)
    assert mean == 0
    assert median == 0
    assert os.path.isfile(plot_path)

    # Test case 8: Valid file path, valid plot path, all negative data
    file_path = "all_negative_data.csv"
    plot_path = "plot.png"
    with open(file_path, "w") as f:
        f.write("col1,col2\n-1,-2")
    mean, median, plot_path = task_func(file_path, plot_path)
    assert mean == -1
    assert median == -1
    assert os.path.isfile(plot_path)

    # Test case 9: Valid file path, valid plot path, all positive data
    file_path = "all_positive_data.csv"
    plot_path = "plot.png"
    with open(file_path, "w") as f:
        f.write("col1,col2\n1,2")
    mean, median, plot_path = task_func(file_path, plot_path)
    assert mean == 1
    assert median == 1
    assert os.path.isfile(plot_path)

    # Test case 10: Valid file path, valid plot path, mixed data
    file_path = "mixed_data.csv"
    plot_path = "plot.png"
    with open(file_path, "w") as f:
        f.write("col1,col2\n1,2\n3,4\n5,6\n7,8\n9,10")
    mean, median, plot_path = task_func(file_path, plot_path)
    assert mean == 5
    assert median == 5
    assert os.path.isfile(plot_path)