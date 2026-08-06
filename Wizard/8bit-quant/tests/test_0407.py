python
import pytest
from src_0407 import task_func

def test_task_func():
    img_path = "test_image.jpg"
    angle = 90
    
    # Test if file exists
    with pytest.raises(FileNotFoundError):
        task_func("non_existent_file.jpg", angle)
    
    # Test if angle is valid
    with pytest.raises(ValueError):
        task_func(img_path, "invalid_angle")
    
    # Test if function returns valid numpy arrays
    original_img_array, rotated_img_array = task_func(img_path, angle)
    assert isinstance(original_img_array, np.ndarray)
    assert isinstance(rotated_img_array, np.ndarray)