import pytest
from PIL import Image, ImageFilter
import cv2
import numpy as np
import os
def task_func(img_path, blur_radius=5):
    if not os.path.exists(img_path):
        raise FileNotFoundError(f"No file found at {img_path}")

    img = Image.open(img_path)
    img = img.convert("RGB")

    blurred_img = img.filter(ImageFilter.GaussianBlur(blur_radius))
    grey_img = cv2.cvtColor(np.array(blurred_img), cv2.COLOR_RGB2GRAY)

    return np.array(img), np.array(grey_img)
def test_task_func():
    img_path = "path/to/image.jpg"
    blur_radius = 5
    expected_img_shape = (100, 100, 3)
    expected_grey_shape = (100, 100)
    img, grey_img = task_func(img_path, blur_radius)
    assert img.shape == expected_img_shape
    assert grey_img.shape == expected_grey_shape
def test_task_func_file_not_found():
    img_path = "path/to/nonexistent_image.jpg"
    blur_radius = 5
    with pytest.raises(FileNotFoundError):
        task_func(img_path, blur_radius)