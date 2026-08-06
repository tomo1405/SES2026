import pytest
from src_0427 import task_func

def test_task_func():
    # Test case 1: Test if threshold is an integer between 0 and 255
    with pytest.raises(ValueError):
        task_func(threshold=256)
    with pytest.raises(ValueError):
        task_func(threshold=-1)
    with pytest.raises(ValueError):
        task_func(threshold=10.5)
    with pytest.raises(ValueError):
        task_func(threshold='abc')

    # Test case 2: Test if image_path is a valid file path
    with pytest.raises(FileNotFoundError):
        task_func(image_path='invalid_image.jpg')

    # Test case 3: Test if the function returns the expected output
    image_path = 'image.jpg'
    threshold = 128
    img, binary_img = task_func(image_path, threshold)
    assert isinstance(img, np.ndarray)
    assert isinstance(binary_img, np.ndarray)