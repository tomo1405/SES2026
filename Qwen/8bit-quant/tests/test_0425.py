import pytest
from src_0425 import task_func
import os
import numpy as np
import cv2

# Mocking functions and classes
class MockKMeans:
    def __init__(self, n_clusters, random_state):
        self.n_clusters = n_clusters
        self.random_state = random_state
        self.labels_ = np.array([0, 1, 2])
        self.cluster_centers_ = np.array([[0, 0, 0], [255, 255, 255], [128, 128, 128]])

    def fit(self, X):
        pass

def mock_cv2_imread(image_path):
    if image_path == 'image.jpg':
        return np.array([[0, 0, 0], [255, 255, 255]], dtype=np.uint8)
    else:
        return None

def mock_os_path_exists(image_path):
    return image_path == 'image.jpg'

# Patching
@pytest.fixture(autouse=True)
def patch_dependencies(monkeypatch):
    monkeypatch.setattr(cv2, 'imread', mock_cv2_imread)
    monkeypatch.setattr(os.path, 'exists', mock_os_path_exists)
    monkeypatch.setattr('sklearn.cluster.KMeans', MockKMeans)

def test_task_func_valid_input():
    original_img, segmented_img = task_func(image_path='image.jpg', n_clusters=3, random_seed=42)
    assert isinstance(original_img, np.ndarray)
    assert isinstance(segmented_img, np.ndarray)
    assert original_img.shape == (2, 3)
    assert segmented_img.shape == (2, 3)

def test_task_func_n_clusters_one():
    original_img, segmented_img = task_func(image_path='image.jpg', n_clusters=1, random_seed=42)
    assert np.array_equal(original_img, segmented_img)

def test_task_func_invalid_n_clusters():
    with pytest.raises(ValueError, match="n_clusters must be a positive integer."):
        task_func(image_path='image.jpg', n_clusters=0, random_seed=42)

def test_task_func_nonexistent_image():
    with pytest.raises(FileNotFoundError, match="No image found at non_existent.jpg"):
        task_func(image_path='non_existent.jpg', n_clusters=3, random_seed=42)

def test_task_func_failed_to_read_image():
    with pytest.raises(ValueError, match="Failed to read the image file."):
        task_func(image_path='invalid_image.jpg', n_clusters=3, random_seed=42)

def test_task_func_saves_cluster_images(tmpdir):
    task_func(image_path='image.jpg', n_clusters=3, random_seed=42)
    for i in range(1, 4):
        assert os.path.exists(f'cluster_{i}.jpg')