import pytest
from src_0404 import task_func
from PIL import Image, ImageFilter
import cv2
import numpy as np
import os
import tempfile

def create_temp_image():
    with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_file:
        image = Image.new('RGB', (100, 100), color='red')
        image.save(temp_file.name)
    return temp_file.name

def test_task_func_valid_image():
    img_path = create_temp_image()
    original_img, grey_img = task_func(img_path)
    
    assert isinstance(original_img, np.ndarray)
    assert isinstance(grey_img, np.ndarray)
    assert original_img.shape == (100, 100, 3)
    assert grey_img.shape == (100, 100)

    # Clean up the temporary file
    os.remove(img_path)

def test_task_func_nonexistent_image():
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func("nonexistent_image.png")
    assert str(excinfo.value) == "No file found at nonexistent_image.png"

def test_task_func_invalid_image_format():
    with tempfile.NamedTemporaryFile(delete=False, suffix='.txt') as temp_file:
        with open(temp_file.name, 'w') as f:
            f.write("This is not an image file.")
    
    with pytest.raises(Exception) as excinfo:
        task_func(temp_file.name)
    assert "cannot identify image file" in str(excinfo.value)

    # Clean up the temporary file
    os.remove(temp_file.name)