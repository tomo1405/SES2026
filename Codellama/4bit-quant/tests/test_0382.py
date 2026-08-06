import pytest
from src_0382 import task_func

def test_task_func():
    # Test that the function raises an error if the file does not exist
    with pytest.raises(FileNotFoundError):
        task_func(file_path='invalid_file.csv')

    # Test that the function raises an error if the target column does not exist
    with pytest.raises(ValueError):
        task_func(file_path='arena.csv', target_column='invalid_column')

    # Test that the function returns the correct plot and importances
    ax, importances = task_func(file_path='arena.csv', target_column='Index')
    assert isinstance(ax, matplotlib.axes.Axes)
    assert isinstance(importances, numpy.ndarray)
    assert importances.shape == (X.shape[1],)