import pytest
from src_0426 import task_func
import os
import cv2
import matplotlib.pyplot as plt
import numpy as np

@pytest.fixture
def create_test_image(tmpdir):
    # Create a temporary test image
    img = np.zeros((100, 100), dtype=np.uint8)
    cv2.rectangle(img, (25, 25), (75, 75), 255, -1)
    image_path = tmpdir.join('test_image.jpg')
    cv2.imwrite(str(image_path), img)
    return str(image_path)

def test_task_func(create_test_image, tmpdir):
    image_path = create_test_image
    histogram_path = tmpdir.join('test_histogram.png')

    # Call the function
    axes = task_func(image_path=str(image_path), histogram_path=str(histogram_path))

    # Check if the file was created
    assert os.path.exists(histogram_path)

    # Check if the axes object is returned
    assert isinstance(axes, plt.Axes)

    # Check if the histogram is correct
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    assert np.array_equal(hist, axes.lines[0].get_ydata())

def test_task_func_nonexistent_image(tmpdir):
    image_path = tmpdir.join('nonexistent_image.jpg')
    histogram_path = tmpdir.join('test_histogram.png')

    with pytest.raises(FileNotFoundError) as excinfo:
        task_func(image_path=str(image_path), histogram_path=str(histogram_path))

    assert f"No image found at {image_path}" in str(excinfo.value)