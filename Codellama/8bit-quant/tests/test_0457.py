import pytest
from src_0457 import task_func
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

def test_task_func():
    # Test case 1: Normal data
    data = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    expected_data = pd.DataFrame({"A": [0.5, 1, 1.5], "B": [0.75, 1, 1.25]})
    expected_ax = plt.Axes(figsize=(10, 8))
    expected_ax.set_title("Normalized Data")
    expected_ax.set_xlabel("Features")
    expected_ax.set_ylabel("Normalized Values")
    expected_ax.set_xticks([0, 1, 2])
    expected_ax.set_yticks([0, 0.5, 1])
    expected_ax.set_xticklabels(["A", "B", "C"])
    expected_ax.set_yticklabels(["0", "0.5", "1"])
    expected_ax.set_ylim([0, 1])
    expected_ax.set_xlim([0, 2])
    expected_ax.set_cmap("YlGnBu")
    expected_ax.set_label("Normalized Value")

    normalized_data, ax = task_func(data)

    assert normalized_data.equals(expected_data)
    assert ax.get_title() == expected_ax.get_title()
    assert ax.get_xlabel() == expected_ax.get_xlabel()
    assert ax.get_ylabel() == expected_ax.get_ylabel()
    assert ax.get_xticks() == expected_ax.get_xticks()
    assert ax.get_yticks() == expected_ax.get_yticks()
    assert ax.get_xticklabels() == expected_ax.get_xticklabels()
    assert ax.get_yticklabels() == expected_ax.get_yticklabels()
    assert ax.get_ylim() == expected_ax.get_ylim()
    assert ax.get_xlim() == expected_ax.get_xlim()
    assert ax.get_cmap() == expected_ax.get_cmap()
    assert ax.get_label() == expected_ax.get_label()