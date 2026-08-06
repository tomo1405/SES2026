import pytest
from src_0432 import task_func

def test_task_func_valid_image():
    image_file = "test_image.jpg"
    expected_histogram = np.array([100, 100, 100, 100, 100, 100, 100, 100, 100, 100])
    histogram = task_func(image_file)
    assert np.array_equal(histogram, expected_histogram)

def test_task_func_invalid_image():
    image_file = "invalid_image.jpg"
    with pytest.raises(ValueError):
        task_func(image_file)

def test_task_func_non_existent_image():
    image_file = "non_existent_image.jpg"
    with pytest.raises(FileNotFoundError):
        task_func(image_file)