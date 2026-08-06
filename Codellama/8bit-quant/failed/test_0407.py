import pytest
from src_0407 import task_func

def test_task_func():
    # Test case 1: Valid input
    img_path = 'path/to/image.jpg'
    angle = 45
    original_img_array, rotated_img_array = task_func(img_path, angle)
    assert isinstance(original_img_array, np.ndarray)
    assert isinstance(rotated_img_array, np.ndarray)
    assert original_img_array.shape == rotated_img_array.shape

    # Test case 2: Invalid input
    img_path = 'path/to/invalid/image.jpg'
    angle = 45
    with pytest.raises(FileNotFoundError):
        task_func(img_path, angle)

    # Test case 3: Valid input with angle = 0
    img_path = 'path/to/image.jpg'
    angle = 0
    original_img_array, rotated_img_array = task_func(img_path, angle)
    assert isinstance(original_img_array, np.ndarray)
    assert isinstance(rotated_img_array, np.ndarray)
    assert original_img_array.shape == rotated_img_array.shape

    # Test case 4: Valid input with angle = 360
    img_path = 'path/to/image.jpg'
    angle = 360
    original_img_array, rotated_img_array = task_func(img_path, angle)
    assert isinstance(original_img_array, np.ndarray)
    assert isinstance(rotated_img_array, np.ndarray)
    assert original_img_array.shape == rotated_img_array.shape

    # Test case 5: Valid input with angle = 90
    img_path = 'path/to/image.jpg'
    angle = 90
    original_img_array, rotated_img_array = task_func(img_path, angle)
    assert isinstance(original_img_array, np.ndarray)
    assert isinstance(rotated_img_array, np.ndarray)
    assert original_img_array.shape == rotated_img_array.shape

    # Test case 6: Valid input with angle = 180
    img_path = 'path/to/image.jpg'
    angle = 180
    original_img_array, rotated_img_array = task_func(img_path, angle)
    assert isinstance(original_img_array, np.ndarray)
    assert isinstance(rotated_img_array, np.ndarray)
    assert original_img_array.shape == rotated_img_array.shape

    # Test case 7: Valid input with angle = 270
    img_path = 'path/to/image.jpg'
    angle = 270
    original_img_array, rotated_img_array = task_func(img_path, angle)
    assert isinstance(original_img_array, np.ndarray)
    assert isinstance(rotated_img_array, np.ndarray)
    assert original_img_array.shape == rotated_img_array.shape