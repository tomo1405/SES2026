import pytest
from src_0450 import task_func
import pandas as pd
import matplotlib.pyplot as plt

# Mocking matplotlib to avoid actual plotting
@pytest.fixture
def mock_plt(mocker):
    mocker.patch('matplotlib.pyplot.subplots')
    return mocker

def test_task_func(mock_plt):
    # Create a sample DataFrame
    data = pd.DataFrame({
        "Feature1": [1, 2, 3, 4, 5],
        "Feature2": [5, 4, 3, 2, 1],
        "Feature3": [2, 3, 4, 5, 6],
        "Feature4": [6, 5, 4, 3, 2],
        "Feature5": [3, 4, 5, 6, 7]
    })

    # Call the function
    standardized_data, axes_list = task_func(data)

    # Check if the returned DataFrame is standardized
    assert isinstance(standardized_data, pd.DataFrame)
    assert all(standardized_data.columns == ["Feature1", "Feature2", "Feature3", "Feature4", "Feature5"])
    assert standardized_data.shape == data.shape

    # Check if the mean and std of each feature are approximately zero and one, respectively
    for feature in standardized_data.columns:
        assert standardized_data[feature].mean() == pytest.approx(0)
        assert standardized_data[feature].std() == pytest.approx(1)

    # Check if the axes list is created correctly
    assert isinstance(axes_list, list)
    assert len(axes_list) == 5
    for ax in axes_list:
        assert isinstance(ax, plt.Axes)

    # Check if subplots were called correctly
    mock_plt.subplots.assert_called_with()
    assert mock_plt.subplots.call_count == 5