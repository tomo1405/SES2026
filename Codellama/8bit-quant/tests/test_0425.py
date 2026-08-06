import pytest
from src_0425 import task_func


def test_task_func_positive_n_clusters():
    image_path = 'image.jpg'
    n_clusters = 3
    random_seed = 42
    img, segmented_image = task_func(image_path, n_clusters, random_seed)
    assert isinstance(img, np.ndarray)
    assert isinstance(segmented_image, np.ndarray)
    assert img.shape == segmented_image.shape


def test_task_func_negative_n_clusters():
    image_path = 'image.jpg'
    n_clusters = -1
    random_seed = 42
    with pytest.raises(ValueError):
        task_func(image_path, n_clusters, random_seed)


def test_task_func_invalid_image_path():
    image_path = 'invalid_image.jpg'
    n_clusters = 3
    random_seed = 42
    with pytest.raises(FileNotFoundError):
        task_func(image_path, n_clusters, random_seed)


def test_task_func_invalid_image_file():
    image_path = 'image.jpg'
    n_clusters = 3
    random_seed = 42
    with pytest.raises(ValueError):
        task_func(image_path, n_clusters, random_seed)


def test_task_func_n_clusters_equal_to_1():
    image_path = 'image.jpg'
    n_clusters = 1
    random_seed = 42
    img, segmented_image = task_func(image_path, n_clusters, random_seed)
    assert isinstance(img, np.ndarray)
    assert isinstance(segmented_image, np.ndarray)
    assert img.shape == segmented_image.shape


def test_task_func_n_clusters_greater_than_1():
    image_path = 'image.jpg'
    n_clusters = 3
    random_seed = 42
    img, segmented_image = task_func(image_path, n_clusters, random_seed)
    assert isinstance(img, np.ndarray)
    assert isinstance(segmented_image, np.ndarray)
    assert img.shape == segmented_image.shape
    assert len(os.listdir()) == n_clusters