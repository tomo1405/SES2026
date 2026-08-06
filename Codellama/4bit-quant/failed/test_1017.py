import pytest
from src_1017 import task_func

def test_task_func_valid_url():
    url = "https://example.com/image.jpg"
    ax = task_func(url)
    assert isinstance(ax, matplotlib.axes._axes.Axes)
    assert ax.get_title() == "Grayscale Histogram"
    assert ax.get_xlabel() == "Pixel Value"
    assert ax.get_ylabel() == "Frequency"

def test_task_func_invalid_url():
    url = "invalid_url"
    with pytest.raises(ValueError):
        task_func(url)

def test_task_func_download_error():
    url = "https://example.com/image.jpg"
    with pytest.raises(ValueError):
        task_func(url)

def test_task_func_image_processing_error():
    url = "https://example.com/image.jpg"
    with pytest.raises(IOError):
        task_func(url)