import pytest
from src_0243 import task_func

def test_task_func():
    # Test 1: Invalid kernel size
    with pytest.raises(ValueError):
        task_func('image.jpg', -1)

    # Test 2: Valid kernel size
    image, ax1, ax2 = task_func('image.jpg', 3)
    assert isinstance(image, np.ndarray)
    assert isinstance(ax1, plt.Axes)
    assert isinstance(ax2, plt.Axes)

    # Test 3: Invalid image path
    with pytest.raises(FileNotFoundError):
        task_func('invalid_image.jpg', 3)