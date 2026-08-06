import pytest
from src_0404 import task_func
from PIL import Image
import numpy as np
import os

def test_task_func_valid_image(tmpdir):
    # Create a temporary image file
    img_path = str(tmpdir.join('test_image.png'))
    image = Image.new('RGB', (100, 100), color = 'red')
    image.save(img_path)

    original_img, grey_img = task_func(img_path)

    assert isinstance(original_img, np.ndarray)
    assert isinstance(grey_img, np.ndarray)
    assert original_img.shape == (100, 100, 3)
    assert grey_img.shape == (100, 100)

def test_task_func_invalid_image():
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func('non_existent_file.png')
    
    assert str(excinfo.value) == "No file found at non_existent_file.png"

def test_task_func_blur_radius(tmpdir):
    img_path = str(tmpdir.join('test_image.png'))
    image = Image.new('RGB', (100, 100), color = 'red')
    image.save(img_path)

    original_img, grey_img = task_func(img_path, blur_radius=10)

    assert isinstance(original_img, np.ndarray)
    assert isinstance(grey_img, np.ndarray)
    assert original_img.shape == (100, 100, 3)
    assert grey_img.shape == (100, 100)