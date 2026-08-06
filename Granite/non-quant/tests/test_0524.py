import pandas as pd
import matplotlib.pyplot as plt
import pytest

def task_func(data):
    if not data:
        return None
    df = pd.DataFrame(data)
    plt.figure()
    for label in df.columns:
        plt.plot(df[label], label=label)
    plt.xlabel("Time")
    plt.ylabel("Data Points")
    plt.title("Data over Time")
    return plt.gca()

def test_task_func():
    data = {'Label 1': [1, 2, 3], 'Label 2': [4, 5, 6]}
    expected_output = ' axes object'
    actual_output = task_func(data)
    assert isinstance(actual_output, str) and actual_output == expected_output, "Expected output is a string containing 'axes object', but the actual output is different."
    data = {}
    expected_output = None
    actual_output = task_func(data)
    assert actual_output == expected_output, "Expected output is None, but the actual output is different."