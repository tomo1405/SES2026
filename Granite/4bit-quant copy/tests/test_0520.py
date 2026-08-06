import pandas as pd
import matplotlib.pyplot as plt
import pytest

def task_func(data):
    df = pd.DataFrame(data)
    df.fillna(0, inplace=True)
    for fruit in df.columns:
        plt.plot(df[fruit], label=fruit)
    plt.xlabel("Time")
    plt.ylabel("Sales Quantity")
    plt.title("Fruit Sales over Time")
    plt.legend()
    return plt.gca()

def test_task_func():
    data = {'apple': [1, 2, 3], 'banana': [4, 5, 6]}
    ax = task_func(data)
    assert ax.get_xlabel() == "Time"
    assert ax.get_ylabel() == "Sales Quantity"
    assert ax.get_title() == "Fruit Sales over Time"
    assert len(ax.get_lines()) == 2
    assert ax.get_lines()[0].get_label() == "apple"
    assert ax.get_lines()[1].get_label() == "banana"