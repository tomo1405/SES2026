import pytest
from src_0432 import task_func

def test_task_func_valid_image():
    image_file = "path/to/image.jpg"
    histogram = task_func(image_file)
    assert histogram.shape == (256,)
    assert np.all(histogram >= 0)

def test_task_func_invalid_image():
    image_file = "path/to/invalid_image.jpg"
    with pytest.raises(ValueError):
        task_func(image_file)

def test_task_func_non_existent_image():
    image_file = "path/to/non_existent_image.jpg"
    with pytest.raises(FileNotFoundError):
        task_func(image_file)