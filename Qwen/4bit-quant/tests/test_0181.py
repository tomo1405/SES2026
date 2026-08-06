import matplotlib.pyplot as plt
import numpy as np
import pytest
from PIL import Image
from src_0181 import task_func


def test_task_func_file_not_found():
    with pytest.raises(FileNotFoundError):
        task_func('non_existent_path.jpg')

def test_task_func_valid_image(tmpdir):
    # Create a temporary image file
    img_path = tmpdir.join('test_image.jpg')
    img = Image.new('RGB', (100, 100), color='red')
    img.save(img_path)

    results = task_func(str(img_path))

    assert isinstance(results, list)
    assert len(results) == 4  # Default number of scale factors

    for ax, scaled_img_arr in results:
        assert isinstance(ax, plt.Axes)
        assert isinstance(scaled_img_arr, np.ndarray)

def test_task_func_custom_scale_factors(tmpdir):
    # Create a temporary image file
    img_path = tmpdir.join('test_image.jpg')
    img = Image.new('RGB', (100, 100), color='red')
    img.save(img_path)

    custom_scale_factors = [0.25, 0.5]
    results = task_func(str(img_path), custom_scale_factors)

    assert isinstance(results, list)
    assert len(results) == len(custom_scale_factors)

    for ax, scaled_img_arr in results:
        assert isinstance(ax, plt.Axes)
        assert isinstance(scaled_img_arr, np.ndarray)