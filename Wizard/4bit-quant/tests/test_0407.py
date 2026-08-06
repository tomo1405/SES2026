python
import pytest
from src_0407 import task_func

def test_task_func():
    # Test case 1: Valid input
    img_path = 'test_image.jpg'
    angle = 90
    original_img_array, rotated_img_array = task_func(img_path, angle)
    assert original_img_array.shape == rotated_img_array.shape
    assert original_img_array.shape == (100, 100, 3)

    # Test case 2: Invalid input (file not found)
    img_path = 'invalid_file.jpg'
    angle = 90
    with pytest.raises(FileNotFoundError):
        task_func(img_path, angle)

    # Test case 3: Invalid input (angle not a number)
    img_path = 'test_image.jpg'
    angle = 'not_a_number'
    with pytest.raises(ValueError):
        task_func(img_path, angle)