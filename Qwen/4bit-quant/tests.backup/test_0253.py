import pytest
from src_0253 import task_func
import matplotlib.pyplot as plt
import io
import sys

@pytest.fixture
def mock_plt(mocker):
    # Mocking the matplotlib.pyplot module to capture plot actions
    mock_plt = mocker.patch('matplotlib.pyplot')
    return mock_plt

def test_task_func_with_valid_data(mock_plt):
    data = [[1, 2, 3], [4, 5, 6]]
    labels = ['Series 1', 'Series 2']
    
    ax = task_func(data, labels)
    
    # Check if subplots were created
    mock_plt.subplots.assert_called_once()
    
    # Check if plot was called with correct arguments
    mock_plt.plot.assert_has_calls([
        mocker.call([1, 2, 3], label='Series 1', color='red'),
        mocker.call([4, 5, 6], label='Series 2', color='green')
    ])
    
    # Check if legend was called
    mock_plt.legend.assert_called_once()
    
    # Check if the axis object is returned
    assert ax == mock_plt.subplots.return_value[1]

def test_task_func_with_more_labels_than_colors(mock_plt):
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    labels = ['Series 1', 'Series 2', 'Series 3']
    
    ax = task_func(data, labels)
    
    # Check if plot was called with correct arguments, including default color for extra labels
    mock_plt.plot.assert_has_calls([
        mocker.call([1, 2, 3], label='Series 1', color='red'),
        mocker.call([4, 5, 6], label='Series 2', color='green'),
        mocker.call([7, 8, 9], label='Series 3', color='black')
    ])

def test_task_func_with_less_labels_than_data(mock_plt):
    data = [[1, 2, 3], [4, 5, 6]]
    labels = ['Series 1']
    
    ax = task_func(data, labels)
    
    # Check if plot was called with correct arguments, using default colors for missing labels
    mock_plt.plot.assert_has_calls([
        mocker.call([1, 2, 3], label='Series 1', color='red'),
        mocker.call([4, 5, 6], label=None, color='green')
    ])

def test_task_func_with_no_data(mock_plt):
    data = []
    labels = ['Series 1']
    
    ax = task_func(data, labels)
    
    # Check if plot was not called
    mock_plt.plot.assert_not_called()

def test_task_func_with_no_labels(mock_plt):
    data = [[1, 2, 3], [4, 5, 6]]
    labels = []
    
    ax = task_func(data, labels)
    
    # Check if plot was called with correct arguments, using default colors for missing labels
    mock_plt.plot.assert_has_calls([
        mocker.call([1, 2, 3], label=None, color='red'),
        mocker.call([4, 5, 6], label=None, color='green')
    ])