import pytest
from src_0426 import task_func
import os
import matplotlib.pyplot as plt

@pytest.fixture
def create_test_image(tmpdir):
    # Create a simple test image
    image_path = tmpdir.join('test_image.jpg')
    img = [[0, 128, 255], [0, 128, 255], [0, 128, 255]]
    cv2.imwrite(str(image_path), img)
    return str(image_path)

def test_task_func(create_test_image, tmpdir):
    histogram_path = str(tmpdir.join('test_histogram.png'))
    axes = task_func(create_test_image, histogram_path)
    
    assert os.path.exists(histogram_path), "Histogram file was not created"
    
    # Check if the plot has the correct title and labels
    assert axes.get_title() == "Grayscale Histogram"
    assert axes.get_xlabel() == "Bins"
    assert axes.get_ylabel() == "# of Pixels"

def test_task_func_non_existent_image():
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func('non_existent_image.jpg')
    assert "No image found at non_existent_image.jpg" in str(excinfo.value)