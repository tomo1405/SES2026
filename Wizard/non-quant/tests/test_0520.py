python
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
    data = {'apple': [10, 20, 30], 'banana': [5, 10, 15], 'orange': [2, 4, 6]}
    fig = task_func(data)
    assert isinstance(fig, plt.Axes)