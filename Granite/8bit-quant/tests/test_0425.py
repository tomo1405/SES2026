import cv2
import numpy as np
import os
from sklearn.cluster import KMeans
import pytest

from src_0425 import task_func

@pytest.fixture
def image_path():
    return 'image.jpg'

@pytest.fixture
def n_clusters():
    return 3

@pytest.fixture
def random_seed():
    return 42

def test_task_func_with_valid_input(image_path, n_clusters, random_seed):
    img, segmented_image = task_func(image_path, n_clusters, random_seed)
    assert isinstance(img, np.ndarray)
    assert isinstance(segmented_image, np.ndarray)
    assert img.shape == segmented_image.shape
    assert img.dtype == segmented_image.dtype

def test_task_func_with_invalid_n_clusters(image_path, random_seed):
    with pytest.raises(ValueError) as exc_info:
        task_func(image_path, 'invalid_n_clusters', random_seed)
    assert 'n_clusters must be a positive integer.' in str(exc_info.value)

def test_task_func_with_nonexistent_image_path(n_clusters, random_seed):
    with pytest.raises(FileNotFoundError) as exc_info:
        task_func('nonexistent_image.jpg', n_clusters, random_seed)
    assert f"No image found at nonexistent_image.jpg" in str(exc_info.value)

def test_task_func_with_invalid_image_file(image_path, n_clusters, random_seed):
    invalid_image_path = os.path.join(os.path.dirname(image_path), 'invalid_image.jpg')
    cv2.imwrite(invalid_image_path, np.zeros((100, 100, 3), dtype=np.uint8))
    with pytest.raises(ValueError) as exc_info:
        task_func(invalid_image_path, n_clusters, random_seed)
    assert "Failed to read the image file." in str(exc_info.value)
    os.remove(invalid_image_path)

def test_task_func_with_n_clusters_equals_to_one(image_path, random_seed):
    img, segmented_image = task_func(image_path, 1, random_seed)
    assert np.array_equal(img, segmented_image)

def test_task_func_with_n_clusters_greater_than_one(image_path, n_clusters, random_seed):
    img, segmented_image = task_func(image_path, n_clusters, random_seed)
    assert not np.array_equal(img, segmented_image)

def test_task_func_with_n_clusters_greater_than_one_and_save_images(image_path, n_clusters, random_seed):
    img, segmented_image = task_func(image_path, n_clusters, random_seed)
    assert os.path.exists('cluster_1.jpg')
    assert os.path.exists('cluster_2.jpg')
    assert os.path.exists('cluster_3.jpg')