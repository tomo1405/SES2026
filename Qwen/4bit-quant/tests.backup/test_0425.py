import pytest
from src_0425 import task_func
import os
import cv2
import numpy as np

def test_task_func_invalid_n_clusters():
    with pytest.raises(ValueError, match="n_clusters must be a positive integer."):
        task_func(n_clusters=-1)

def test_task_func_nonexistent_image():
    with pytest.raises(FileNotFoundError, match="No image found at non_existent_image.jpg"):
        task_func(image_path='non_existent_image.jpg')

def test_task_func_failed_to_read_image():
    with pytest.raises(ValueError, match="Failed to read the image file."):
        task_func(image_path='invalid_image_path.jpg')

def test_task_func_single_cluster():
    original_img, segmented_img = task_func(n_clusters=1)
    assert np.array_equal(original_img, segmented_img), "Original and segmented images should be the same for 1 cluster."

def test_task_func_multiple_clusters():
    original_img, segmented_img = task_func(n_clusters=3)
    assert original_img.shape == segmented_img.shape, "Original and segmented images should have the same shape."
    assert np.array_equal(original_img, cv2.imread('image.jpg')), "Original image should match the input image."
    assert np.array_equal(segmented_img, cv2.imread('cluster_1.jpg')), "Segmented image should match the first cluster image."

def test_task_func_cluster_images_exist():
    task_func(n_clusters=3)
    for i in range(1, 4):
        assert os.path.exists(f'cluster_{i}.jpg'), f"Cluster {i} image does not exist."

def test_task_func_cleanup():
    task_func(n_clusters=3)
    for i in range(1, 4):
        os.remove(f'cluster_{i}.jpg')