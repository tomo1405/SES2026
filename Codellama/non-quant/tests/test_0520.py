import pytest
from src_0520 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func():
    data = {
        "Apple": [1, 2, 3, 4, 5],
        "Banana": [10, 20, 30, 40, 50],
        "Orange": [100, 200, 300, 400, 500]
    }
    df = pd.DataFrame(data)
    df.fillna(0, inplace=True)
    for fruit in df.columns:
        plt.plot(df[fruit], label=fruit)
    plt.xlabel("Time")
    plt.ylabel("Sales Quantity")
    plt.title("Fruit Sales over Time")
    plt.legend()
    plt.gca()
    assert plt.gca().get_title() == "Fruit Sales over Time"
    assert plt.gca().get_xlabel() == "Time"
    assert plt.gca().get_ylabel() == "Sales Quantity"
    assert plt.gca().get_legend().get_title().get_text() == "Fruit"
    assert plt.gca().get_legend().get_texts()[0].get_text() == "Apple"
    assert plt.gca().get_legend().get_texts()[1].get_text() == "Banana"
    assert plt.gca().get_legend().get_texts()[2].get_text() == "Orange"