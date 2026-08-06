from datetime import datetime
from unittest.mock import patch

from src_0597 import task_func


@patch('matplotlib.pyplot.show')
@patch('matplotlib.pyplot.pause')
@patch('matplotlib.pyplot.draw')
@patch('matplotlib.pyplot.clf')
@patch('matplotlib.pyplot.plot')
@patch('time.time')
@patch('random.randint')
def test_task_func(mock_randint, mock_time, mock_plot, mock_clf, mock_draw, mock_pause, mock_show):
    # Mocking constants
    VALUES_RANGE = (0, 100)
    PLOT_INTERVAL = 0.1

    # Mocking time.time to control the loop
    mock_time.side_effect = [0, 0.1, 0.2, 0.3, 1]  # Simulate time passing

    # Mocking randint to return predictable values
    mock_randint.side_effect = [10, 20, 30, 40]

    # Expected output
    expected_x_data = [
        datetime.fromtimestamp(0).strftime('%H:%M:%S.%f'),
        datetime.fromtimestamp(0.1).strftime('%H:%M:%S.%f'),
        datetime.fromtimestamp(0.2).strftime('%H:%M:%S.%f'),
        datetime.fromtimestamp(0.3).strftime('%H:%M:%S.%f')
    ]
    expected_y_data = [10, 20, 30, 40]

    # Call the function
    x_data, y_data = task_func(duration=1)

    # Assertions
    assert x_data == expected_x_data
    assert y_data == expected_y_data

    # Verify that plot methods were called correctly
    mock_plot.assert_called_with(expected_x_data, expected_y_data)
    assert mock_clf.call_count == 4
    assert mock_draw.call_count == 4
    assert mock_pause.call_count == 4
    mock_show.assert_called_once()