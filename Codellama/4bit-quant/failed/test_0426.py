import pytest
from src_0426 import task_func

def test_task_func():
    # Test that the function raises an error if the image path is invalid
    with pytest.raises(FileNotFoundError):
        task_func(image_path='invalid_image.jpg')

    # Test that the function raises an error if the histogram path is invalid
    with pytest.raises(FileNotFoundError):
        task_func(histogram_path='invalid_histogram.png')

    # Test that the function returns the correct axes object
    image_path = 'image.jpg'
    histogram_path = 'histogram.png'
    axes = task_func(image_path, histogram_path)
    assert isinstance(axes, plt.Axes)
    assert axes.title.get_text() == 'Grayscale Histogram'
    assert axes.xlabel.get_text() == 'Bins'
    assert axes.ylabel.get_text() == '# of Pixels'

    # Test that the function saves the histogram to the correct path
    histogram_path = 'histogram.png'
    task_func(image_path, histogram_path)
    assert os.path.exists(histogram_path)