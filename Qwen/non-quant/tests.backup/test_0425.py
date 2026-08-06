import pytest
from src_0425 import task_func
import cv2
import numpy as np
import os

def test_task_func_invalid_n_clusters():
    with pytest.raises(ValueError):
        task_func(n_clusters=0)

def test_task_func_nonexistent_image_path():
    with pytest.raises(FileNotFoundError):
        task_func(image_path='nonexistent.jpg')

def test_task_func_failed_to_read_image():
    # Create a dummy image path that cv2.imread will fail to read
    dummy_path = 'dummy.jpg'
    with open(dummy_path, 'w') as f:
        f.write('not an image')
    with pytest.raises(ValueError):
        task_func(image_path=dummy_path)
    os.remove(dummy_path)

def test_task_func_single_cluster():
    # Create a small dummy image
    dummy_path = 'dummy.jpg'
    img = np.zeros((10, 10, 3), dtype=np.uint8)
    cv2.imwrite(dummy_path, img)
    original, segmented = task_func(image_path=dummy_path, n_clusters=1)
    assert np.array_equal(original, img)
    assert np.array_equal(segmented, img)
    os.remove(dummy_path)

def test_task_func_multiple_clusters():
    # Create a small dummy image with distinct colors
    dummy_path = 'dummy.jpg'
    img = np.zeros((10, 10, 3), dtype=np.uint8)
    img[0:5, 0:5] = [255, 0, 0]  # Red
    img[5:10, 0:5] = [0, 255, 0]  # Green
    img[0:5, 5:10] = [0, 0, 255]  # Blue
    img[5:10, 5:10] = [255, 255, 0]  # Yellow
    cv2.imwrite(dummy_path, img)
    original, segmented = task_func(image_path=dummy_path, n_clusters=4)
    assert np.array_equal(original, img)
    assert segmented.shape == img.shape
    assert segmented.dtype == np.uint8
    # Check if cluster images are created
    for i in range(1, 5):
        assert os.path.exists(f'cluster_{i}.jpg')
        os.remove(f'cluster_{i}.jpg')
    os.remove(dummy_path)