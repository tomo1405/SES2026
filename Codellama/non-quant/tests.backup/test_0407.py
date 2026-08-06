import pytest
from src_0407 import task_func

def test_task_func():
    # Test case 1: Valid image path and angle
    img_path = 'path/to/image.jpg'
    angle = 45
    original_img_array, rotated_img_array = task_func(img_path, angle)
    assert isinstance(original_img_array, np.ndarray)
    assert isinstance(rotated_img_array, np.ndarray)
    assert original_img_array.shape == rotated_img_array.shape

    # Test case 2: Invalid image path
    img_path = 'path/to/invalid/image.jpg'
    angle = 45
    with pytest.raises(FileNotFoundError):
        task_func(img_path, angle)

    # Test case 3: Invalid angle
    img_path = 'path/to/image.jpg'
    angle = 450
    with pytest.raises(ValueError):
        task_func(img_path, angle)