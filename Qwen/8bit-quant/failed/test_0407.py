import pytest
from src_0407 import task_func
from PIL import Image
import numpy as np
import os

# Mocking the Image class from PIL to avoid actual file operations
class MockImage:
    def __init__(self, size):
        self.size = size

    def rotate(self, angle, expand=True):
        return self

    def __array__(self):
        return np.zeros((self.size[1], self.size[0], 3), dtype=np.uint8)

def test_task_func_file_not_found(mocker):
    mocker.patch('os.path.exists', return_value=False)
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func('non_existent_path.jpg', 90)
    assert str(excinfo.value) == "No file found at non_existent_path.jpg"

def test_task_func_rotation(mocker):
    mock_image = MockImage(size=(100, 100))
    mocker.patch('PIL.Image.open', return_value=mock_image)
    original_array, rotated_array = task_func('test_image.jpg', 90)
    assert original_array.shape == (100, 100, 3)
    assert rotated_array.shape == (100, 100, 3)

def test_task_func_no_rotation(mocker):
    mock_image = MockImage(size=(100, 100))
    mocker.patch('PIL.Image.open', return_value=mock_image)
    original_array, rotated_array = task_func('test_image.jpg', 0)
    assert np.array_equal(original_array, rotated_array)

def test_task_func_expanded_rotation(mocker):
    mock_image = MockImage(size=(100, 100))
    mocker.patch('PIL.Image.open', return_value=mock_image)
    original_array, rotated_array = task_func('test_image.jpg', 45)
    assert original_array.shape == (100, 100, 3)
    assert rotated_array.shape != (100, 100, 3)