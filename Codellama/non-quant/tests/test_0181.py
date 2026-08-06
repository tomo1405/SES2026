import pytest
from src_0181 import task_func

def test_task_func():
    img_path = 'path/to/image.jpg'
    scale_factors = [0.5, 0.75, 1.5, 2.0]
    results = task_func(img_path, scale_factors)
    assert len(results) == len(scale_factors)
    for ax, scaled_img_arr in results:
        assert ax.get_title() == f'Scale factor: {scale_factor}'
        assert scaled_img_arr.shape == (int(im.height * scale_factor), int(im.width * scale_factor))