import pytest
from src_0612 import task_func
import pandas as pd
from unittest.mock import patch, MagicMock

@pytest.fixture
def sample_df():
    data = {
        'A': [1, 2, 3, 4],
        'B': [5, 6, 7, 8],
        'C': [9, 10, 11, 12],
        'D': [13, 14, 15, 16],
        'E': [17, 18, 19, 20]
    }
    return pd.DataFrame(data)

@pytest.fixture
def sample_tuples():
    return [(1, 5), (3, 7)]

@patch('src_0612.sample')
@patch('matplotlib.pyplot.show')
def test_task_func(mock_show, mock_sample, sample_df, sample_tuples):
    mock_sample.return_value = ['A', 'B']
    
    result_df, plot_details = task_func(sample_df, sample_tuples, 2)
    
    # Check that the correct number of rows are removed
    assert len(result_df) == 2
    
    # Check that the correct columns are plotted
    assert plot_details == [('A', 'B')]
    
    # Check that plt.show() is called
    mock_show.assert_called_once()
    
    # Check that sample is called with the correct arguments
    mock_sample.assert_called_with(['A', 'B', 'C', 'D', 'E'], 2)

@patch('src_0612.sample')
@patch('matplotlib.pyplot.show')
def test_task_func_no_rows_removed(mock_show, mock_sample, sample_df, sample_tuples):
    mock_sample.return_value = ['A', 'B']
    
    result_df, plot_details = task_func(sample_df, [(5, 6), (7, 8)], 2)
    
    # Check that no rows are removed
    assert len(result_df) == 4
    
    # Check that the correct columns are plotted
    assert plot_details == [('A', 'B')]
    
    # Check that plt.show() is called
    mock_show.assert_called_once()
    
    # Check that sample is called with the correct arguments
    mock_sample.assert_called_with(['A', 'B', 'C', 'D', 'E'], 2)

@patch('src_0612.sample')
@patch('matplotlib.pyplot.show')
def test_task_func_zero_plots(mock_show, mock_sample, sample_df, sample_tuples):
    mock_sample.return_value = ['A', 'B']
    
    result_df, plot_details = task_func(sample_df, sample_tuples, 0)
    
    # Check that the correct number of rows are removed
    assert len(result_df) == 2
    
    # Check that no plots are generated
    assert plot_details == []
    
    # Check that plt.show() is not called
    mock_show.assert_not_called()
    
    # Check that sample is not called
    mock_sample.assert_not_called()