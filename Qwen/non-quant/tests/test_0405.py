import pytest
from src_0405 import task_func
import cv2
import numpy as np
import os
import tempfile

def test_task_func_non_existent_file():
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func("non_existent_file.jpg")
    assert "No file found at non_existent_file.jpg" in str(excinfo.value)

def test_task_func_valid_image():
    # Create a temporary image file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as temp_file:
        img_path = temp_file.name
        # Create a simple black image
        img = np.zeros((100, 100, 3), dtype=np.uint8)
        cv2.imwrite(img_path, img)
        
        # Call the function
        original_img, contours = task_func(img_path)
        
        # Check if the original image is returned correctly
        assert np.array_equal(original_img, img)
        
        # Check if contours are found (for a black image, contours should be empty)
        assert len(contours) == 0
        
        # Clean up the temporary file
        os.remove(img_path)