import pytest
from src_0404 import task_func
from PIL import Image, ImageFilter
import cv2
import numpy as np
import os

def test_task_func():
    # Test case 1: Normal case
    img_path = 'test_image.png'
    # Create a dummy image for testing
    img = Image.new('RGB', (100, 100), color = (255, 255, 255))
    img.save(img_path)
    
    result = task_func(img_path)
    assert isinstance(result, tuple), "The result should be a tuple"
    assert len(result) == 2, "The result should contain two elements"
    assert isinstance(result[0], np.ndarray), "The first element should be a numpy array"
    assert isinstance(result[1], np.ndarray), "The second element should be a numpy array"
    
    # Clean up
    os.remove(img_path)

    # Test case 2: File not found
    with pytest.raises(FileNotFoundError):
        task_func('nonexistent_image.png')