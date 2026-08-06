import pytest
from src_0424 import task_func

def test_task_func():
    # Test 1: Threshold is not an integer
    with pytest.raises(ValueError):
        task_func(threshold=128.5)

    # Test 2: Threshold is not between 0 and 255
    with pytest.raises(ValueError):
        task_func(threshold=-1)

    # Test 3: Image path does not exist
    with pytest.raises(FileNotFoundError):
        task_func(image_path='image.jpg')

    # Test 4: Image path exists but is not a valid image file
    with pytest.raises(ValueError):
        task_func(image_path='image.txt')

    # Test 5: Image path exists and is a valid image file
    img, binary_img = task_func(image_path='image.jpg')
    assert isinstance(img, np.ndarray)
    assert isinstance(binary_img, np.ndarray)
    assert img.shape == binary_img.shape
    assert np.all(binary_img == np.where(img > 128, 255, 0))