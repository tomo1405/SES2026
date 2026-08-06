import pytest
from src_0424 import task_func

def test_task_func_threshold_type():
    with pytest.raises(ValueError):
        task_func(threshold='128')

def test_task_func_threshold_range():
    with pytest.raises(ValueError):
        task_func(threshold=-1)
    with pytest.raises(ValueError):
        task_func(threshold=256)

def test_task_func_image_path():
    with pytest.raises(FileNotFoundError):
        task_func(image_path='image.jpg')

def test_task_func_image_path_and_threshold():
    img, binary_img = task_func(image_path='image.jpg', threshold=128)
    assert isinstance(img, np.ndarray)
    assert isinstance(binary_img, np.ndarray)
    assert img.shape == binary_img.shape
    assert np.all(binary_img == np.where(img > 128, 255, 0))