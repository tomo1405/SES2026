import pytest
from src_0425 import task_func
import cv2
import numpy as np
import os
from sklearn.cluster import KMeans

def test_task_func_basic():
    # Test basic functionality
    img_path = 'test_image.jpg'
    n_clusters = 3
    result = task_func(image_path=img_path, n_clusters=n_clusters)
    assert isinstance(result, tuple), "The function should return a tuple."
    assert len(result) == 2, "The function should return a tuple with two elements."
    assert isinstance(result[0], np.ndarray), "The first element should be a numpy array."
    assert isinstance(result[1], np.ndarray), "The second element should be a numpy array."

def test_invalid_image_path():
    with pytest.raises(FileNotFoundError):
        task_func(image_path='nonexistent_image.jpg', n_clusters=3)

def test_invalid_n_clusters():
    with pytest.raises(ValueError):
        task_func(image_path='test_image.jpg', n_clusters=0)

def test_single_cluster():
    result = task_func(image_path='test_image.jpg', n_clusters=1)
    assert np.array_equal(result[0], result[1]), "The images should be the same when n_clusters is 1."

def test_multiple_clusters():
    result = task_func(image_path='test_image.jpg', n_clusters=3)
    assert len(result) == 2, "The function should return a tuple with two elements."
    assert isinstance(result[0], np.ndarray), "The first element should be a numpy array."
    assert isinstance(result[1], np.ndarray), "The second element should be a numpy array."