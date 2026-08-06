import pandas as pd
import matplotlib.pyplot as plt
import pytest

def task_func(csv_file_path: str):
    df = pd.read_csv(csv_file_path)
    mean = df["column1"].mean()
    std = df["column1"].std()
    df["column1_normalized"] = (df["column1"] - mean) / std

    _, ax = plt.subplots()
    ax.plot(df["column1_normalized"])
    title = "%*s : %*s" % (20, "Plot Title", 20, "Normalized Column 1")
    xlabel = "%*s : %*s" % (20, "Index", 20, "Normalized Value")
    ylabel = "%*s : %*s" % (20, "Frequency", 20, "Normalized Value")
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    return ax

def test_task_func():
    csv_file_path = "path/to/csv/file.csv"
    ax = task_func(csv_file_path)
    assert ax is not None
    assert ax.get_title() == "%*s : %*s" % (20, "Plot Title", 20, "Normalized Column 1")
    assert ax.get_xlabel() == "%*s : %*s" % (20, "Index", 20, "Normalized Value")
    assert ax.get_ylabel() == "%*s : %*s" % (20, "Frequency", 20, "Normalized Value")