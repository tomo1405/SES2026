import pytest
from src_0215 import task_func

def test_task_func():
    # Test that the function returns an Axes object and a NumPy array
    ax, image = task_func()
    assert isinstance(ax, plt.Axes)
    assert isinstance(image, np.ndarray)

    # Test that the image has the correct shape
    assert image.shape == (100, 100, 3)

    # Test that the image is within the correct range
    assert np.all(image >= 0)
    assert np.all(image <= 255)

    # Test that the image is a valid RGB image
    assert np.all(image[:, :, 0] >= 0)
    assert np.all(image[:, :, 0] <= 255)
    assert np.all(image[:, :, 1] >= 0)
    assert np.all(image[:, :, 1] <= 255)
    assert np.all(image[:, :, 2] >= 0)
    assert np.all(image[:, :, 2] <= 255)

    # Test that the image is not all zeros
    assert not np.all(image == 0)

    # Test that the image is not all ones
    assert not np.all(image == 255)