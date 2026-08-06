python
import pandas as pd
import matplotlib.pyplot as plt
import pytest

def task_func(csv_file_path: str):
    df = pd.read_csv(csv_file_path)
    mean = df["column1"].mean()
    std = df["column1"].std()
    df["column1_normalized"] = (df["column1"] - mean) / std

    # Creating a figure and axes
    _, ax = plt.subplots()
    # Plotting on the created axes
    ax.plot(df["column1_normalized"])
    title = "%*s : %*s" % (20, "Plot Title", 20, "Normalized Column 1")
    xlabel = "%*s : %*s" % (20, "Index", 20, "Normalized Value")
    ylabel = "%*s : %*s" % (20, "Frequency", 20, "Normalized Value")
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    # Return the axes object for further manipulation
    return ax

def test_task_func():
    # Test case 1: Test with valid input file
    csv_file_path = "test_data.csv"
    ax = task_func(csv_file_path)
    assert ax is not None
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Plot Title : Normalized Column 1"
    assert ax.get_xlabel() == "Index : Normalized Value"
    assert ax.get_ylabel() == "Frequency : Normalized Value"
    assert ax.lines[0].get_data()[0][0] == 0
    assert ax.lines[0].get_data()[1][0] == 0.5
    assert ax.lines[0].get_data()[0][1] == 1
    assert ax.lines[0].get_data()[1][1] == 1.5
    assert ax.lines[0].get_data()[0][2] == 2
    assert ax.lines[0].get_data()[1][2] == 2.5
    assert ax.lines[0].get_data()[0][3] == 3
    assert ax.lines[0].get_data()[1][3] == 3.5
    assert ax.lines[0].get_data()[0][4] == 4
    assert ax.lines[0].get_data()[1][4] == 4.5
    assert ax.lines[0].get_data()[0][5] == 5
    assert ax.lines[0].get_data()[1][5] == 5.5
    assert ax.lines[0].get_data()[0][6] == 6
    assert ax.lines[0].get_data()[1][6] == 6.5
    assert ax.lines[0].get_data()[0][7] == 7
    assert ax.lines[0].get_data()[1][7] == 7.5
    assert ax.lines[0].get_data()[0][8] == 8
    assert ax.lines[0].get_data()[1][8] == 8.5
    assert ax.lines[0].get_data()[0][9] == 9
    assert ax.lines[0].get_data()[1][9] == 9.5
    assert ax.lines[0].get_data()[0][10] == 10
    assert ax.lines[0].get_data()[1][10] == 10.5
    assert ax.lines[0].get_data()[0][11] == 11
    assert ax.lines[0].get_data()[1][11] == 11.5
    assert ax.lines[0].get_data()[0][12] == 12
    assert ax.lines[0].get_data()[1][12] == 12.5
    assert ax.lines[0].get_data()[0][13] == 13
    assert ax.lines[0].get_data()[1][13] == 13.5
    assert ax.lines[0].get_data()[0][14] == 14
    assert ax.lines[0].get_data()[1][14] == 14.5
    assert ax.lines[0].get_data()[0][15] == 15
    assert ax.lines[0].get_data()[1][15] == 15.5
    assert ax.lines[0].get_data()[0][16] == 16
    assert ax.lines[0].get_data()[1][16] == 16.5
    assert ax.lines[0].get_data()[0][17] == 17
    assert ax.lines[0].get_data()[1][17] == 17.5
    assert ax.lines[0].get_data()[0][18] == 18
    assert ax.lines[0].get_data()[1][18] == 18.5
    assert ax.lines[0].get_data()[0][19] == 19
    assert ax.lines[0].get_data()[1][19] == 19.5

    # Test case 2: Test with invalid input file
    csv_file_path = "invalid_file.csv"
    with pytest.raises(FileNotFoundError):
        task_func(csv_file_path)