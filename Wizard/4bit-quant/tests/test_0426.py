python
import cv2
import os
import pytest
from matplotlib import pyplot as plt

def task_func(image_path='image.jpg', histogram_path='histogram.png'):

    if not os.path.exists(image_path):
        raise FileNotFoundError(f"No image found at {image_path}")

    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])

    plt.figure()
    plt.title("Grayscale Histogram")
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")
    axes = plt.plot(hist)[0].axes
    plt.savefig(histogram_path)
    return axes

def test_task_func():
    with pytest.raises(FileNotFoundError):
        task_func(image_path='invalid_image.jpg')

    axes = task_func()
    assert isinstance(axes, plt.Axes)