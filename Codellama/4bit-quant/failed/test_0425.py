import pytest
from src_0425 import task_func

def test_task_func():
    # Test with valid input
    image_path = 'image.jpg'
    n_clusters = 3
    random_seed = 42
    img, segmented_image = task_func(image_path, n_clusters, random_seed)
    assert isinstance(img, np.ndarray)
    assert isinstance(segmented_image, np.ndarray)
    assert img.shape == segmented_image.shape

    # Test with invalid input
    with pytest.raises(ValueError):
        task_func(image_path, -1, random_seed)
    with pytest.raises(FileNotFoundError):
        task_func('invalid_image.jpg', n_clusters, random_seed)
    with pytest.raises(ValueError):
        task_func(image_path, n_clusters, random_seed, 'invalid_image.jpg')

def test_task_func_n_clusters():
    # Test with n_clusters = 1
    image_path = 'image.jpg'
    n_clusters = 1
    random_seed = 42
    img, segmented_image = task_func(image_path, n_clusters, random_seed)
    assert isinstance(img, np.ndarray)
    assert isinstance(segmented_image, np.ndarray)
    assert img.shape == segmented_image.shape

    # Test with n_clusters > 1
    image_path = 'image.jpg'
    n_clusters = 3
    random_seed = 42
    img, segmented_image = task_func(image_path, n_clusters, random_seed)
    assert isinstance(img, np.ndarray)
    assert isinstance(segmented_image, np.ndarray)
    assert img.shape == segmented_image.shape
    assert len(os.listdir('.')) == n_clusters + 1

def test_task_func_random_seed():
    # Test with random_seed = 42
    image_path = 'image.jpg'
    n_clusters = 3
    random_seed = 42
    img, segmented_image = task_func(image_path, n_clusters, random_seed)
    assert isinstance(img, np.ndarray)
    assert isinstance(segmented_image, np.ndarray)
    assert img.shape == segmented_image.shape

    # Test with random_seed = 1337
    image_path = 'image.jpg'
    n_clusters = 3
    random_seed = 1337
    img, segmented_image = task_func(image_path, n_clusters, random_seed)
    assert isinstance(img, np.ndarray)
    assert isinstance(segmented_image, np.ndarray)
    assert img.shape == segmented_image.shape

if __name__ == '__main__':
    pytest.main()