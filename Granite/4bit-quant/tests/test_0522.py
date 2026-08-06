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
        {"Name": "John", "Test 1": 85, "Test 2": 92, "Test 3": 78},
        {"Name": "Alice", "Test 1": 95, "Test 2": 88, "Test 3": 92},
        {"Name": "Bob", "Test 1": 75, "Test 2": 82, "Test 3": 87}
    ]
    ax = task_func(data_list)
    assert ax.get_title() == "Student Scores over Tests"
    assert ax.get_xlabel() == "Test Number"
    assert ax.get_ylabel() == "Score"
    assert len(ax.get_lines()) == 3
    assert ax.get_lines()[0].get_label() == "Name"
    assert ax.get_lines()[1].get_label() == "Test 1"
    assert ax.get_lines()[2].get_label() == "Test 2"