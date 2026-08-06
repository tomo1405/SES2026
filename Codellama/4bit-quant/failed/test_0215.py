import pytest
from src_0215 import task_func

def test_task_func():
    # Test that the function returns an Axes object and a numpy array
    ax, image = task_func()
    assert isinstance(ax, matplotlib.axes.Axes)
    assert isinstance(image, np.ndarray)

    # Test that the image is the correct size
    assert image.shape == (100, 100, 3)

    # Test that the image is within the correct range
    assert np.all(image >= 0)
    assert np.all(image <= 255)

    # Test that the function raises an error when the range is invalid
    with pytest.raises(ValueError):
        task_func(range_low=256, range_high=257)