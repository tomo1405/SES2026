import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from src_0450 import task_func
import pytest

def test_task_func():
    # Create a sample DataFrame
    data = pd.DataFrame({
        "Feature1": [1, 2, 3, 4, 5],
        "Feature2": [5, 4, 3, 2, 1],
        "Feature3": [10, 20, 30, 40, 50],
        "Feature4": [50, 40, 30, 20, 10],
        "Feature5": [100, 200, 300, 400, 500]
    })

    # Call the function and store the returned values
    data_standardized, axes_list = task_func(data)

    # Check if the returned values have the correct types
    assert isinstance(data_standardized, pd.DataFrame)
    assert isinstance(axes_list, list)

    # Check if the returned DataFrame has the correct columns
    assert all(col in data_standardized.columns for col in ["Feature1", "Feature2", "Feature3", "Feature4", "Feature5"])

    # Check if the returned list contains the correct number of axes objects
    assert len(axes_list) == 5

    # Check if the title of each axes object is correct
    for ax, feature in zip(axes_list, ["Feature1", "Feature2", "Feature3", "Feature4", "Feature5"]):
        assert ax.get_title() == "Histogram of {}".format(feature)