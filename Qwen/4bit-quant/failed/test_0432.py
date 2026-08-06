import pytest
from src_0432 import task_func
import numpy as np
import os

def test_task_func_valid_image(tmp_path):
    # Create a temporary image file
    image_path = tmp_path / "test_image.png"
    height, width = 100, 100
    img = np.zeros((height, width), dtype=np.uint8)
    img[50:, 50:] = 255  # Create a simple binary image
    cv2.imwrite(str(image_path), img)

    # Call the function and check the output
    histogram = task_func(str(image_path))
    assert isinstance(histogram, np.ndarray)
    assert histogram.shape == (256,)
    assert histogram[0] == 2500  # 100*100-50*50 = 2500 pixels are black
    assert histogram[255] == 2500  # 50*50 pixels are white

def test_task_func_nonexistent_file():
    with pytest.raises(FileNotFoundError, match="The file non_existent_file.png does not exist."):
        task_func("non_existent_file.png")

def test_task_func_invalid_image_file(tmp_path):
    # Create a temporary invalid image file
    image_path = tmp_path / "invalid_image.png"
    with open(image_path, 'w') as f:
        f.write("This is not an image file.")

    with pytest.raises(ValueError, match="Invalid image file."):
        task_func(str(image_path))