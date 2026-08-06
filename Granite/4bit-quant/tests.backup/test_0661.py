import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler
def task_func(x, y, labels):
    scaler = StandardScaler()

    fig, ax = plt.subplots()

    # Iterate over the datasets, scale each, and plot
    for i in range(len(x)):
        # Combine x and y values and scale them
        xy = np.vstack((x[i], y[i])).T  # Transpose to get correct shape for scaling
        xy_scaled = scaler.fit_transform(xy)  # Scale data

        # Plot scaled data
        ax.plot(xy_scaled[:, 0], xy_scaled[:, 1], label=labels[i])

    ax.legend()  # Add a legend to the plot

    return fig  # Return the figure object containing the plot
import pytest

def test_task_func():
    x = [np.array([1, 2, 3]), np.array([4, 5, 6])]
    y = [np.array([2, 3, 4]), np.array([5, 6, 7])]
    labels = ["Label 1", "Label 2"]

    fig = task_func(x, y, labels)

    assert isinstance(fig, plt.Figure)

def test_task_func_with_invalid_input():
    x = [np.array([1, 2, 3]), "not an array"]
    y = [np.array([2, 3, 4]), np.array([5, 6, 7])]
    labels = ["Label 1", "Label 2"]

    with pytest.raises(TypeError):
        task_func(x, y, labels)