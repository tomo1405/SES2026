import pytest
from src_0450 import task_func
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

def test_task_func():
    data = pd.DataFrame({"Feature1": [1, 2, 3, 4, 5], "Feature2": [2, 4, 6, 8, 10], "Feature3": [3, 6, 9, 12, 15], "Feature4": [4, 8, 12, 16, 20], "Feature5": [5, 10, 15, 20, 25]})
    expected_data_standardized = pd.DataFrame({"Feature1": [-1.224744871391589, -0.447213595499958, 0.447213595499958, 1.224744871391589], "Feature2": [-1.224744871391589, -0.447213595499958, 0.447213595499958, 1.224744871391589], "Feature3": [-1.224744871391589, -0.447213595499958, 0.447213595499958, 1.224744871391589], "Feature4": [-1.224744871391589, -0.447213595499958, 0.447213595499958, 1.224744871391589], "Feature5": [-1.224744871391589, -0.447213595499958, 0.447213595499958, 1.224744871391589]})
    expected_axes_list = [plt.subplots()[1], plt.subplots()[1], plt.subplots()[1], plt.subplots()[1], plt.subplots()[1]]

    data_standardized, axes_list = task_func(data)

    assert data_standardized.equals(expected_data_standardized)
    assert axes_list == expected_axes_list