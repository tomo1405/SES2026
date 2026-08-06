import cv2
import os
import numpy as np
import pytest

from src_0432 import task_func

def test_task_func():
    image_file = "test_image.jpg"
    histogram_expected = np.random.randint(0, 256, size=256)

    with open(image_file, "wb") as f:
        f.write(os.urandom(1000))

    img = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError("Invalid image file.")

    histogram_actual = task_func(image_file)

    assert np.array_equal(histogram_actual, histogram_expected)