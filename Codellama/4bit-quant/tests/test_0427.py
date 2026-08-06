import pytest
from src_0427 import task_func

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

    # Test 4: Image is not a valid image file
    with pytest.raises(ValueError):
        task_func(image_path='invalid_image.jpg')

    # Test 5: Image is a valid image file
    img, binary_img = task_func(image_path='image.jpg')
    assert isinstance(img, np.ndarray)
    assert isinstance(binary_img, np.ndarray)
    assert img.shape == binary_img.shape

    # Test 6: Threshold is 0
    img, binary_img = task_func(threshold=0)
    assert np.all(binary_img == 0)

    # Test 7: Threshold is 255
    img, binary_img = task_func(threshold=255)
    assert np.all(binary_img == 255)

    # Test 8: Threshold is 128
    img, binary_img = task_func(threshold=128)
    assert np.all(binary_img == 255)