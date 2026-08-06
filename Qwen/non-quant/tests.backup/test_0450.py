import pytest
from src_0450 import task_func
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

def test_task_func():
    # Create a sample DataFrame
    data = pd.DataFrame({
        "Feature1": [1, 2, 3, 4, 5],
        "Feature2": [5, 4, 3, 2, 1],
        "Feature3": [2, 3, 4, 5, 6],
        "Feature4": [6, 5, 4, 3, 2],
        "Feature5": [3, 4, 5, 6, 7]
    })

    # Call the function
    data_standardized, axes_list = task_func(data)

    # Check that the standardized data is a DataFrame
    assert isinstance(data_standardized, pd.DataFrame)

    # Check that the number of columns in the standardized data matches the input data
    assert len(data_standardized.columns) == len(data.columns)

    # Check that the standardized data has the correct column names
    assert all(col in data_standardized.columns for col in ["Feature1", "Feature2", "Feature3", "Feature4", "Feature5"])

    # Check that the standardized data has the correct number of rows
    assert len(data_standardized) == len(data)

    # Check that the axes_list is a list
    assert isinstance(axes_list, list)

    # Check that the number of axes in the list matches the number of features
    assert len(axes_list) == 5

    # Check that each axis in the list is an Axes object
    for ax in axes_list:
        assert isinstance(ax, plt.Axes)

    # Check that the standardized data has been scaled correctly
    scaler = StandardScaler()
    expected_data_standardized = pd.DataFrame(
        scaler.fit_transform(data[["Feature1", "Feature2", "Feature3", "Feature4", "Feature5"]]),
        columns=["Feature1", "Feature2", "Feature3", "Feature4", "Feature5"]
    )
    assert data_standardized.equals(expected_data_standardized)