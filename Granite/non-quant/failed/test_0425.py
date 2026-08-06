import cv2
import numpy as np
import os
from sklearn.cluster import KMeans
from src_0425 import task_func

def test_task_func_with_valid_input():
    image_path = 'image.jpg'
    n_clusters = 3
    random_seed = 42
    img, segmented_image = task_func(image_path, n_clusters, random_seed)
    assert img.shape == segmented_image.shape == (480, 640, 3)
    assert img.dtype == segmented_image.dtype == np.uint8

def test_task_func_with_invalid_n_clusters():
    image_path = 'image.jpg'
    n_clusters = 0
    random_seed = 42
    try:
        task_func(image_path, n_clusters, random_seed)
    except ValueError as e:
        assert str(e) == "n_clusters must be a positive integer."

def test_task_func_with_invalid_image_path():
    image_path = 'invalid_image.jpg'
    n_clusters = 3
    random_seed = 42
    try:
        task_func(image_path, n_clusters, random_seed)
    except FileNotFoundError as e:
        assert str(e) == f"No image found at {image_path}"

def test_task_func_with_invalid_image_file():
    image_path = 'invalid_image.jpg'
    n_clusters = 3
    random_seed = 42
    with open(image_path, 'w') as f:
        f.write('This is not an image file.')
    try:
        task_func(image_path, n_clusters, random_seed)
    except ValueError as e:
        assert str(e) == "Failed to read the image file."

def test_task_func_with_n_clusters_equals_one():
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
    assert segmented_image.shape == (480, 640, 3)
    assert segmented_image.dtype == np.uint8
    for i in range(n_clusters):
        cluster_img = cv2.imread(f'cluster_{i+1}.jpg')
        assert np.array_equal(cluster_img, segmented_image)