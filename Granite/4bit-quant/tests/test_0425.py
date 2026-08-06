import numpy as np
import pytest
from src_0425 import task_func


def test_task_func_with_valid_input():
    image_path = 'image.jpg'
    n_clusters = 3
    random_seed = 42
    img, segmented_image = task_func(image_path, n_clusters, random_seed)
    assert isinstance(img, np.ndarray)
    assert isinstance(segmented_image, np.ndarray)
    assert img.shape == segmented_image.shape
    assert img.dtype == segmented_image.dtype
    assert img.max() <= 255
    assert img.min() >= 0
    assert segmented_image.max() <= 255
    assert segmented_image.min() >= 0

def test_task_func_with_invalid_n_clusters():
    image_path = 'image.jpg'
    n_clusters = 0
    random_seed = 42
    with pytest.raises(ValueError) as excinfo:
        task_func(image_path, n_clusters, random_seed)
    assert "n_clusters must be a positive integer." in str(excinfo.value)

def test_task_func_with_invalid_image_path():
    image_path = 'invalid_image.jpg'
    n_clusters = 3
    random_seed = 42
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func(image_path, n_clusters, random_seed)
    assert f"No image found at {image_path}" in str(excinfo.value)

def test_task_func_with_invalid_image_read():
    image_path = 'invalid_image.jpg'
    n_clusters = 3
    random_seed = 42
    img, segmented_image = task_func(image_path, n_clusters, random_seed)
    assert img is None
    assert segmented_image is None

def test_task_func_with_one_cluster():
    image_path = 'image.jpg'
    n_clusters = 1
    random_seed = 42
    img, segmented_image = task_func(image_path, n_clusters, random_seed)
    assert np.array_equal(img, segmented_image)

def test_task_func_with_multiple_clusters():
    image_path = 'image.jpg'
    n_clusters = 3
    random_seed = 42
    img, segmented_image = task_func(image_path, n_clusters, random_seed)
    assert not np.array_equal(img, segmented_image)