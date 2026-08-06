import matplotlib.pyplot as plt
import numpy as np
import pytest
from src_0661 import task_func


def test_task_func():
    # Sample data
    x = [np.array([1, 2, 3]), np.array([4, 5, 6])]
    y = [np.array([7, 8, 9]), np.array([10, 11, 12])]
    labels = ['Dataset 1', 'Dataset 2']

    # Call the function
    fig = task_func(x, y, labels)

    # Check if the returned object is a matplotlib Figure
    assert isinstance(fig, plt.Figure)

    # Check if the figure has at least one Axes
    assert len(fig.axes) > 0

    # Check if the plot has the correct number of lines
    ax = fig.axes[0]
    assert len(ax.lines) == len(labels)

    # Check if the legend has the correct labels
    legend_labels = [text.get_text() for text in ax.get_legend().get_texts()]
    assert legend_labels == labels

    # Check if the data points are scaled
    for i in range(len(x)):
        xy = np.vstack((x[i], y[i])).T
        scaler = StandardScaler()
        xy_scaled = scaler.fit_transform(xy)
        line_data = np.column_stack((ax.lines[i].get_xdata(), ax.lines[i].get_ydata()))
        assert np.allclose(line_data, xy_scaled)

# Run the tests
if __name__ == "__main__":
    pytest.main()