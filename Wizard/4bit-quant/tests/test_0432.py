python
import cv2
import os
import numpy as np
import pytest

def task_func(image_file: str) -> np.ndarray:
    if not os.path.exists(image_file):
        raise FileNotFoundError(f"The file {image_file} does not exist.")

    img = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError("Invalid image file.")

    histogram, _ = np.histogram(img.ravel(), bins=256, range=[0,256])
    
    return histogram

def test_task_func():
    with pytest.raises(FileNotFoundError):
        task_func("non_existent_file.jpg")

    with pytest.raises(ValueError):
        task_func("invalid_image.png")

    histogram = task_func("test_image.jpg")
    assert len(histogram) == 256
    assert histogram.sum() == 1000000