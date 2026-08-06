import pytest
from src_0404 import task_func
import os
import numpy as np

def test_task_func_valid_image(tmpdir):
    # Create a temporary directory and add a test image
    tmp_dir = tmpdir.mkdir("test_images")
    test_image_path = str(tmp_dir.join("test_image.png"))
    
    # Create a simple test image
    img = Image.new('RGB', (100, 100), color = 'red')
    img.save(test_image_path)

    original_img, grey_img = task_func(test_image_path)

    assert isinstance(original_img, np.ndarray)
    assert isinstance(grey_img, np.ndarray)
    assert original_img.shape == (100, 100, 3)
    assert grey_img.shape == (100, 100)

def test_task_func_non_existent_image():
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func("non_existent_image.png")
    assert "No file found at non_existent_image.png" in str(excinfo.value)

def test_task_func_invalid_image_format(tmpdir):
    # Create a temporary directory and add a test file that is not an image
    tmp_dir = tmpdir.mkdir("test_files")
    test_file_path = str(tmp_dir.join("test_file.txt"))
    
    with open(test_file_path, 'w') as f:
        f.write("This is a test file.")

    with pytest.raises(Exception) as excinfo:
        task_func(test_file_path)
    assert "cannot identify image file" in str(excinfo.value)