import pytest
from src_0407 import task_func

def test_task_func():
    # Test with valid image path and angle
    img_path = 'path/to/image.jpg'
    angle = 90
    original_img_array, rotated_img_array = task_func(img_path, angle)
    assert isinstance(original_img_array, np.ndarray)
    assert isinstance(rotated_img_array, np.ndarray)
    assert original_img_array.shape == rotated_img_array.shape

    # Test with invalid image path
    img_path = 'path/to/invalid/image.jpg'
    with pytest.raises(FileNotFoundError):
        task_func(img_path, angle)

    # Test with invalid angle
    angle = 360
    with pytest.raises(ValueError):
        task_func(img_path, angle)