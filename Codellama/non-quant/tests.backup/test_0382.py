import pytest
from src_0382 import task_func

def test_task_func():
    # Test that the function raises a FileNotFoundError when the file does not exist
    with pytest.raises(FileNotFoundError):
        task_func(file_path='non_existent_file.csv')

    # Test that the function raises a ValueError when the target column does not exist in the CSV file
    with pytest.raises(ValueError):
        task_func(file_path='arena.csv', target_column='non_existent_column')

    # Test that the function returns a valid matplotlib figure and importances
    ax, importances = task_func(file_path='arena.csv', target_column='Index')
    assert isinstance(ax, plt.Axes)
    assert isinstance(importances, np.ndarray)
    assert importances.shape == (X.shape[1],)