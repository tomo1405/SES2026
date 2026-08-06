import pytest
from src_0215 import task_func

def test_task_func_default_parameters():
    ax, image = task_func()
    assert image.shape == (100, 100, 3)
    assert image.dtype == np.uint8
    assert np.all(image >= 0)
    assert np.all(image <= 255)

def test_task_func_custom_seed():
    seed = 42
    ax1, image1 = task_func(seed=seed)
    ax2, image2 = task_func(seed=seed)
    assert np.array_equal(image1, image2)

def test_task_func_custom_image_size():
    image_size = (50, 50, 3)
    ax, image = task_func(image_size=image_size)
    assert image.shape == image_size

def test_task_func_custom_range():
    range_low = 10
    range_high = 200
    ax, image = task_func(range_low=range_low, range_high=range_high)
    assert np.all(image >= range_low)
    assert np.all(image <= range_high)

def test_task_func_invalid_range():
    with pytest.raises(ValueError):
        task_func(range_low=255, range_high=255)

def test_task_func_invalid_range_order():
    with pytest.raises(ValueError):
        task_func(range_low=255, range_high=0)