import pytest
from src_0432 import task_func
import cv2
import numpy as np
import os

# Mocking os.path.exists and cv2.imread for testing purposes
class TestTaskFunc:
    def test_file_not_found(self, monkeypatch):
        def mock_exists(path):
            return False
        monkeypatch.setattr(os.path, 'exists', mock_exists)

        with pytest.raises(FileNotFoundError) as excinfo:
            task_func('non_existent_file.jpg')
        assert str(excinfo.value) == "The file non_existent_file.jpg does not exist."

    def test_invalid_image_file(self, monkeypatch):
        def mock_imread(path, flags):
            return None
        monkeypatch.setattr(cv2, 'imread', mock_imread)

        with pytest.raises(ValueError) as excinfo:
            task_func('invalid_image_file.jpg')
        assert str(excinfo.value) == "Invalid image file."

    def test_valid_image_file(self, monkeypatch):
        def mock_exists(path):
            return True
        monkeypatch.setattr(os.path, 'exists', mock_exists)

        def mock_imread(path, flags):
            # Create a dummy grayscale image
            return np.zeros((100, 100), dtype=np.uint8)
        monkeypatch.setattr(cv2, 'imread', mock_imread)

        histogram = task_func('valid_image_file.jpg')
        assert isinstance(histogram, np.ndarray)
        assert histogram.shape == (256,)
        assert np.sum(histogram) == 10000  # 100x100 pixels all set to 0