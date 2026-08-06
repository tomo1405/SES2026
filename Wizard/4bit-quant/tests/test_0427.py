python
import pytest
import numpy as np
import cv2
import os

def task_func(image_path='image.jpg', threshold=128):

    if not isinstance(threshold, int) or not (0 <= threshold <= 255):
        raise ValueError("Threshold must be an integer between 0 and 255.")

    if not os.path.exists(image_path):
        raise FileNotFoundError(f"No image found at {image_path}")

    # Image processing
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    binary_img = np.where(img >= threshold, 255, 0).astype('uint8')
    cv2.imwrite('binary_image.jpg', binary_img)

    return np.array(img), np.array(binary_img)

def test_task_func():
    # Test case 1: Valid input
    img, binary_img = task_func('image.jpg', 128)
    assert img.shape == (200, 300)
    assert binary_img.shape == (200, 300)
    assert binary_img.dtype == np.uint8
    assert np.sum(binary_img) == 1000000

    # Test case 2: Invalid input (threshold not an integer)
    with pytest.raises(ValueError):
        task_func('image.jpg', 128.5)

    # Test case 3: Invalid input (threshold out of range)
    with pytest.raises(ValueError):
        task_func('image.jpg', 256)

    # Test case 4: Invalid input (image not found)
    with pytest.raises(FileNotFoundError):
        task_func('invalid_image.jpg', 128)