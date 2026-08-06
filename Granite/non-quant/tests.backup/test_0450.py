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
    # Create a sample DataFrame for testing
    data = pd.DataFrame({
        "Feature1": [1, 2, 3, 4, 5],
        "Feature2": [5, 4, 3, 2, 1],
        "Feature3": [10, 20, 30, 40, 50],
        "Feature4": [50, 40, 30, 20, 10],
        "Feature5": [100, 200, 300, 400, 500]
    })

    # Call the function and store the returned values
    data_standardized, axes_list = task_func(data)

    # Perform assertions to test the function's behavior
    assert isinstance(data_standardized, pd.DataFrame)
    assert len(data_standardized.columns) == 5
    assert isinstance(axes_list, list)
    assert len(axes_list) == 5
    for ax in axes_list:
        assert isinstance(ax, plt.Axes)

if __name__ == "__main__":
    pytest.main()