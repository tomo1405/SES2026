from io import BytesIO

import matplotlib.pyplot as plt
import numpy as np
import pytest
from PIL import Image
from src_0181 import task_func


@pytest.fixture
def test_image():
    # Create a simple test image
    img = Image.new('RGB', (100, 100), color = 'red')
    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    return img_byte_arr

@pytest.fixture
def temp_image_file(test_image, tmpdir):
    img_path = tmpdir.join("test_image.png")
    with open(img_path, 'wb') as f:
        f.write(test_image)
    return str(img_path)

def test_task_func_with_valid_image(temp_image_file):
    results = task_func(temp_image_file)
    assert isinstance(results, list)
    assert len(results) == 4
    for ax, scaled_img_arr in results:
        assert isinstance(ax, plt.Axes)
        assert isinstance(scaled_img_arr, np.ndarray)

def test_task_func_with_non_existent_image():
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func("non_existent_image.png")
    assert "No file found at non_existent_image.png" in str(excinfo.value)

def test_task_func_with_custom_scale_factors(temp_image_file):
    custom_scale_factors = [0.3, 0.6]
    results = task_func(temp_image_file, scale_factors=custom_scale_factors)
    assert isinstance(results, list)
    assert len(results) == 2
    for ax, scaled_img_arr in results:
        assert isinstance(ax, plt.Axes)
        assert isinstance(scaled_img_arr, np.ndarray)