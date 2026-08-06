import pytest
from src_0283 import task_func
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os

def test_task_func_file_not_found():
    with pytest.raises(FileNotFoundError):
        task_func("non_existent_file.jpg", lambda event: None)

def test_task_func_valid_file(mocker):
    mock_img = np.zeros((100, 100, 3), dtype=np.uint8)
    mocker.patch('cv2.imread', return_value=mock_img)
    mock_fig = mocker.Mock()
    mock_ax = mocker.Mock(spec=Axes3D)
    mocker.patch('matplotlib.pyplot.figure', return_value=mock_fig)
    mock_fig.add_subplot.return_value = mock_ax

    def mock_onpick(event):
        pass

    ax = task_func("test_image.jpg", mock_onpick)

    assert isinstance(ax, Axes3D)
    mock_ax.plot.assert_called()
    mock_fig.canvas.mpl_connect.assert_called_with('pick_event', mock_onpick)