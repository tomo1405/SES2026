import pytest
from src_0597 import task_func
from unittest.mock import patch, MagicMock
import matplotlib.pyplot as plt

@patch('matplotlib.pyplot.show')
@patch('matplotlib.pyplot.pause')
@patch('matplotlib.pyplot.draw')
@patch('matplotlib.pyplot.clf')
@patch('matplotlib.pyplot.plot')
@patch('time.time')
@patch('random.randint')
def test_task_func(mock_randint, mock_time, mock_plot, mock_clf, mock_draw, mock_pause, mock_show):
    # Mocking the time.time() to control the loop duration
    mock_time.side_effect = [0, 0.1, 0.2, 0.3, 0.4, 0.5]
    
    # Mocking the random.randint to return predictable values
    mock_randint.return_value = 50
    
    # Expected output
    expected_x_data = [
        '00:00:00.000000', '00:00:00.100000', 
        '00:00:00.200000', '00:00:00.300000', 
        '00:00:00.400000'
    ]
    expected_y_data = [50, 50, 50, 50, 50]
    
    # Call the function
    x_data, y_data = task_func(0.5)
    
    # Assertions
    assert x_data == expected_x_data
    assert y_data == expected_y_data
    
    # Check that the plot functions were called correctly
    mock_plot.assert_called_with(expected_x_data, expected_y_data)
    mock_clf.assert_called()
    mock_draw.assert_called()
    mock_pause.assert_called_with(0.1)
    mock_show.assert_called_once()

# Test with zero duration
@patch('matplotlib.pyplot.show')
def test_task_func_zero_duration(mock_show):
    x_data, y_data = task_func(0)
    assert x_data == []
    assert y_data == []
    mock_show.assert_not_called()