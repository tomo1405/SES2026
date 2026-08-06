import pytest
from src_0283 import task_func
import numpy as np
import cv2
import os

def test_task_func_file_not_found():
    with pytest.raises(FileNotFoundError):
        task_func("non_existent_file.jpg", lambda event: None)

def test_task_func_valid_file(mocker):
    # Mocking cv2.imread to return a dummy image
    mock_image = np.zeros((100, 100, 3), dtype=np.uint8)
    mocker.patch('cv2.imread', return_value=mock_image)

    # Mocking the onpick function
    onpick_mock = mocker.Mock()

    # Call the function
    ax = task_func("dummy_image.jpg", onpick_mock)

    # Check if the plot was created correctly
    assert isinstance(ax, Axes3D)
    assert len(ax.lines) == 3  # One line for each color channel (B, G, R)

    # Check if the onpick event is connected
    assert 'pick_event' in ax.figure.canvas.callbacks.callbacks

def test_task_func_invalid_image_format(mocker):
    # Mocking cv2.imread to return None (invalid image format)
    mocker.patch('cv2.imread', return_value=None)

    with pytest.raises(Exception) as excinfo:
        task_func("dummy_image.jpg", lambda event: None)

    assert "Error reading image" in str(excinfo.value)