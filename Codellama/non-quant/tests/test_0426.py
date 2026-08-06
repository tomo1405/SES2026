import pytest
from src_0426 import task_func

def test_task_func_valid_image():
    image_path = "image.jpg"
    histogram_path = "histogram.png"
    axes = task_func(image_path, histogram_path)
    assert axes is not None

def test_task_func_invalid_image():
    image_path = "invalid_image.jpg"
    histogram_path = "histogram.png"
    with pytest.raises(FileNotFoundError):
        task_func(image_path, histogram_path)

def test_task_func_invalid_histogram_path():
    image_path = "image.jpg"
    histogram_path = "invalid_histogram.png"
    with pytest.raises(FileNotFoundError):
        task_func(image_path, histogram_path)