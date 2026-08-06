python
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import pytest

def task_func(data: pd.DataFrame) -> (pd.DataFrame, list):
    FEATURES = ["Feature1", "Feature2", "Feature3", "Feature4", "Feature5"]

    scaler = StandardScaler()
    data_standardized = pd.DataFrame(
        scaler.fit_transform(data[FEATURES]), columns=FEATURES
    )

    axes_list = []
    for feature in FEATURES:
        fig, ax = plt.subplots()
        ax.hist(data_standardized[feature], bins=20, alpha=0.5)
        ax.set_title("Histogram of {}".format(feature))
        axes_list.append(ax)

    return data_standardized, axes_list

def test_task_func():
    data = pd.DataFrame({"Feature1": [1, 2, 3, 4, 5],
                         "Feature2": [2, 3, 4, 5, 6],
                         "Feature3": [3, 4, 5, 6, 7],
                         "Feature4": [4, 5, 6, 7, 8],
                         "Feature5": [5, 6, 7, 8, 9]})

    data_standardized, axes_list = task_func(data)

    assert isinstance(data_standardized, pd.DataFrame)
    assert isinstance(axes_list, list)
    assert len(axes_list) == len(FEATURES)
    assert isinstance(axes_list[0], plt.Axes)
    assert isinstance(axes_list[1], plt.Axes)
    assert isinstance(axes_list[2], plt.Axes)
    assert isinstance(axes_list[3], plt.Axes)
    assert isinstance(axes_list[4], plt.Axes)