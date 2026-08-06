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
        [90, 85, 92],
        [88, 91, 89],
        [95, 87, 93]
    ]
    ax = task_func(data_list)
    assert ax is not None
    assert ax.get_title() == "Student Scores over Tests"
    assert ax.get_xlabel() == "Test Number"
    assert ax.get_ylabel() == "Score"
    assert len(ax.get_lines()) == 3