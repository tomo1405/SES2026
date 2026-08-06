python
import pandas as pd
import matplotlib.pyplot as plt
import pytest

def task_func(data_list):
    df = pd.DataFrame(data_list)
    fig, ax = plt.subplots()
    for column in df:
        ax.plot(df[column], label=column)
    ax.set_title("Student Scores over Tests")
    ax.set_xlabel("Test Number")
    ax.set_ylabel("Score")

    return ax

def test_task_func():
    data_list = [
        {"Test 1": 80, "Test 2": 70, "Test 3": 90},
        {"Test 1": 75, "Test 2": 85, "Test 3": 95},
        {"Test 1": 90, "Test 2": 80, "Test 3": 85},
    ]
    ax = task_func(data_list)
    assert ax.get_title() == "Student Scores over Tests"
    assert ax.get_xlabel() == "Test Number"
    assert ax.get_ylabel() == "Score"
    assert ax.get_legend_handles_labels()[0] == ["Test 1", "Test 2", "Test 3"]
    assert ax.get_legend_handles_labels()[1] == [80, 70, 90, 75, 85, 95, 90, 80, 85]