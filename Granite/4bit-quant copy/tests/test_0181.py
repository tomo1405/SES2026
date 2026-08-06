import pytest
from PIL import Image
import numpy as np
from skimage.transform import resize
import matplotlib.pyplot as plt
import os

def task_func(img_path, scale_factors=[0.5, 0.75, 1.5, 2.0]):
    if not os.path.exists(img_path):
        raise FileNotFoundError(f"No file found at {img_path}")

    im = Image.open(img_path)
    img_arr = np.array(im)
    results = []

    for scale_factor in scale_factors:
        scaled_img_arr = resize(img_arr, (int(im.height * scale_factor), int(im.width * scale_factor)),
                                mode='reflect', anti_aliasing=True)
        fig, ax = plt.subplots()
        ax.imshow(scaled_img_arr)
        ax.set_title(f'Scale factor: {scale_factor}')
        results.append((ax, scaled_img_arr))
    # plt.show()
    return results

def test_task_func():
    img_path = "path/to/image.jpg"
    scale_factors = [0.5, 0.75, 1.5, 2.0]
    results = task_func(img_path, scale_factors)
    assert len(results) == len(scale_factors)
    for ax, scaled_img_arr in results:
        assert isinstance(ax, plt.Axes)
        assert isinstance(scaled_img_arr, np.ndarray)

def test_task_func_file_not_found():
    img_path = "path/to/nonexistent_image.jpg"
    scale_factors = [0.5, 0.75, 1.5, 2.0]
    with pytest.raises(FileNotFoundError):
        task_func(img_path, scale_factors)