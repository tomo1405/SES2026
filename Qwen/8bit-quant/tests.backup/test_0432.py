import pytest
from src_0432 import task_func
import numpy as np
import cv2
import os

# Mocking cv2.imread to simulate image reading
class MockImageReader:
    def __init__(self, return_value):
        self.return_value = return_value

    def imread(self, *args, **kwargs):
        return self.return_value

@pytest.fixture
def mock_cv2(monkeypatch):
    # Create a mock image array
    mock_image = np.zeros((100, 100), dtype=np.uint8)
    mock_cv2 = MockImageReader(mock_image)
    monkeypatch.setattr(cv2, 'imread', mock_cv2.imread)
    return mock_cv2

def test_task_func_valid_image(mock_cv2, tmp_path):
    # Create a temporary image file
    image_file = tmp_path / "test_image.png"
    cv2.imwrite(str(image_file), np.zeros((100, 100), dtype=np.uint8))

    histogram = task_func(str(image_file))
    assert isinstance(histogram, np.ndarray)
    assert histogram.shape == (256,)
    assert np.sum(histogram) == 10000  # Total number of pixels in the image

def test_task_func_invalid_image_file(tmp_path):
    image_file = tmp_path / "nonexistent_image.png"
    with pytest.raises(FileNotFoundError):
        task_func(str(image_file))

def test_task_func_invalid_image_format(mock_cv2, tmp_path):
    # Simulate an invalid image format by returning None
    mock_cv2.return_value = None
    image_file = tmp_path / "invalid_image.png"
    cv2.imwrite(str(image_file), np.zeros((100, 100), dtype=np.uint8))

    with pytest.raises(ValueError):
        task_func(str(image_file))