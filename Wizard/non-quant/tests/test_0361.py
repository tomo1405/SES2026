python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

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

# Test case 1
def test_task_func_1():
    file_location = "data.xlsx"
    sheet_name = "Sheet1"
    result, fig = task_func(file_location, sheet_name)
    assert result == {'A': {'mean': 1.0, 'std': 0.0}, 'B': {'mean': 2.0, 'std': 0.0}, 'C': {'mean': 3.0, 'std': 0.0}}
    assert isinstance(fig, plt.Figure)

# Test case 2
def test_task_func_2():
    file_location = "data.xlsx"
    sheet_name = "Sheet2"
    try:
        result, fig = task_func(file_location, sheet_name)
    except ValueError as e:
        assert str(e) == "Error reading sheet: 'Sheet2' is not a sheet name"
    else:
        assert False, "Expected ValueError"

# Test case 3
def test_task_func_3():
    file_location = "non_existent_file.xlsx"
    sheet_name = "Sheet1"
    try:
        result, fig = task_func(file_location, sheet_name)
    except FileNotFoundError as e:
        assert str(e) == "No file found at non_existent_file.xlsx"
    else:
        assert False, "Expected FileNotFoundError"