python
import numpy as np
import seaborn as sns
import pytest

def task_func(arr):
    row_sums = arr.sum(axis=1)
    vmax = np.max(arr)  # Set vmax to the maximum value in the array
    vmin = np.min(arr)  # Set vmin to the minimum value in the array
    ax = sns.heatmap(
        arr, annot=True, vmax=vmax, vmin=vmin
    )  # Include both vmin and vmax in the heatmap call
    ax.set_title("Heatmap of the 2D Array")

    return ax

def test_task_func():
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    ax = task_func(arr)
    assert ax is not None
    assert isinstance(ax, sns.matrix.ClusterGrid)
    assert ax.data2d.shape == arr.shape
    assert ax.data2d.max() == arr.max()
    assert ax.data2d.min() == arr.min()
    assert ax.ax_heatmap.get_title() == "Heatmap of the 2D Array"