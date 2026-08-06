import pytest
from src_0425 import task_func

def test_task_func():
    # Test with valid input
    img_path = 'image.jpg'
    n_clusters = 3
    random_seed = 42
    img, segmented_image = task_func(img_path, n_clusters, random_seed)
    assert isinstance(img, np.ndarray)
    assert isinstance(segmented_image, np.ndarray)
    assert img.shape == segmented_image.shape

    # Test with invalid input
    with pytest.raises(ValueError):
        task_func(img_path, 0, random_seed)
    with pytest.raises(ValueError):
        task_func(img_path, 'a', random_seed)
    with pytest.raises(FileNotFoundError):
        task_func('invalid_path.jpg', n_clusters, random_seed)
    with pytest.raises(ValueError):
        task_func(img_path, n_clusters, 'a')