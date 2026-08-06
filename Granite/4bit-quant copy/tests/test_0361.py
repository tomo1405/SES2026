import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import pytest

def task_func(file_location, sheet_name):
    if not os.path.exists(file_location):
        raise FileNotFoundError(f"No file found at {file_location}")

    try:
        df = pd.read_excel(file_location, sheet_name=sheet_name)
    except ValueError as e:
        raise ValueError(f"Error reading sheet: {e}")

    result = {}
    fig, ax = plt.subplots()
    for column in df.columns:
        mean = np.mean(df[column])
        std = np.std(df[column])
        result[column] = {"mean": mean, "std": std}

        ax.bar(column, mean, yerr=std)

    ax.set_title('Mean and Standard Deviation')
    ax.set_xlabel('Columns')
    ax.set_ylabel('Values')

    return result, fig

def test_task_func():
    file_location = "path/to/file.xlsx"
    sheet_name = "Sheet1"
    expected_result = {"column1": {"mean": 10, "std": 2}, "column2": {"mean": 20, "std": 3}}
    expected_fig = "instance of matplotlib.figure.Figure"

    result, fig = task_func(file_location, sheet_name)

    assert result == expected_result
    assert type(fig) == str(expected_fig)

if __name__ == "__main__":
    pytest.main()