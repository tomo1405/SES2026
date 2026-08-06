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
    # Test case 1: Test if the function returns the correct data type
    data = pd.DataFrame({
        "Feature1": [1, 2, 3, 4, 5],
        "Feature2": [5, 4, 3, 2, 1],
        "Feature3": [10, 20, 30, 40, 50],
        "Feature4": [50, 40, 30, 20, 10],
        "Feature5": [100, 200, 300, 400, 500]
    })
    expected_data_standardized = pd.DataFrame({
        "Feature1": [-1.3416407864998738, -0.7625587102715576, -0.18347663404324138, 0.3956054421850748, 0.9746875184133911],
        "Feature2": [0.9746875184133911, 0.3956054421850748, -0.18347663404324138, -0.7625587102715576, -1.3416407864998738],
        "Feature3": [1.3416407864998738, 0.7625587102715576, 0.18347663404324138, -0.3956054421850748, -0.9746875184133911],
        "Feature4": [-0.9746875184133911, -0.3956054421850748, 0.18347663404324138, 0.7625587102715576, 1.3416407864998738],
        "Feature5": [0.9746875184133911, 0.3956054421850748, -0.18347663404324138, -0.7625587102715576, -1.3416407864998738]
    })
    expected_axes_list = [None] * 5
    data_standardized, axes_list = task_func(data)
    assert isinstance(data_standardized, pd.DataFrame)
    assert data_standardized.equals(expected_data_standardized)
    assert isinstance(axes_list, list)
    assert len(axes_list) == 5
    assert all(ax is None for ax in axes_list)

    # Test case 2: Test if the function returns the correct number of histograms
    data = pd.DataFrame({
        "Feature1": [1, 2, 3, 4, 5],
        "Feature2": [5, 4, 3, 2, 1],
        "Feature3": [10, 20, 30, 40, 50],
        "Feature4": [50, 40, 30, 20, 10],
        "Feature5": [100, 200, 300, 400, 500]
    })
    data_standardized, axes_list = task_func(data)
    assert len(axes_list) == 5

    # Test case 3: Test if the function returns the correct histogram titles
    data = pd.DataFrame({
        "Feature1": [1, 2, 3, 4, 5],
        "Feature2": [5, 4, 3, 2, 1],
        "Feature3": [10, 20, 30, 40, 50],
        "Feature4": [50, 40, 30, 20, 10],
        "Feature5": [100, 200, 300, 400, 500]
    })
    data_standardized, axes_list = task_func(data)
    expected_titles = ["Histogram of Feature1", "Histogram of Feature2", "Histogram of Feature3", "Histogram of Feature4", "Histogram of Feature5"]
    for ax, expected_title in zip(axes_list, expected_titles):
        assert ax.get_title() == expected_title

if __name__ == "__main__":
    pytest.main()