import cv2
import os
import pytest
from matplotlib import pyplot as plt
from src_0426 import task_func

def test_task_func():
    image_path = 'image.jpg'
    histogram_path = 'histogram.png'
    with pytest.raises(FileNotFoundError):
        task_func(image_path='nonexistent_image.jpg', histogram_path=histogram_path)
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    plt.figure()
    plt.title("Grayscale Histogram")
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")
    axes = plt.plot(hist)[0].axes
    plt.savefig(histogram_path)
    assert task_func(image_path=image_path, histogram_path=histogram_path) == axes