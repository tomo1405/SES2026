import pytest
from src_0405 import task_func
import os
import numpy as np

def test_task_func_file_not_found():
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func("non_existent_path.jpg")
    assert "No file found at non_existent_path.jpg" in str(excinfo.value)

def test_task_func_valid_image(tmpdir):
    # Create a temporary directory and a test image
    tmp_dir = tmpdir.mkdir("test_images")
    test_image_path = str(tmp_dir.join("test_image.png"))
    
    # Create a simple black image
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.imwrite(test_image_path, img)
    
    # Call the function
    result_img, contours = task_func(test_image_path)
    
    # Check if the returned image is the same as the input image
    assert np.array_equal(result_img, img)
    
    # Check if contours are returned as a numpy array
    assert isinstance(contours, np.ndarray)

def test_task_func_invalid_image_format(tmpdir):
    # Create a temporary directory and a test image with invalid format
    tmp_dir = tmpdir.mkdir("test_images")
    test_image_path = str(tmp_dir.join("test_image.txt"))
    
    # Create a simple text file
    with open(test_image_path, 'w') as f:
        f.write("This is a test file.")
    
    with pytest.raises(cv2.error):
        task_func(test_image_path)