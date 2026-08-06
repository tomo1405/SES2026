import pytest
from src_0424 import task_func

def test_task_func_valid_input():
    # Test with valid input
    image_path = 'test_image.jpg'
    threshold = 128
    expected_output = (np.array([[128]]), np.array([[0]]))
    result = task_func(image_path=image_path, threshold=threshold)
    assert result == expected_output

def test_invalid_threshold():
    # Test with invalid threshold
    image_path = 'test_image.jpg'
    threshold = 256  # Invalid threshold
    with pytest.raises(ValueError):
        task_func(image_path=image_path, threshold=threshold)

def test_file_not_found():
    # Test with non-existent image file
    image_path = 'nonexistent_image.jpg'
    threshold = 128
    with pytest.raises(FileNotFoundError):
        task_func(image_path=image_path, threshold=threshold)