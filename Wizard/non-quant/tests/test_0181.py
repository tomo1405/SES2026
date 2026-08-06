python
import pytest
from src_0181 import task_func

def test_task_func():
    img_path = "test_image.jpg"
    scale_factors = [0.5, 0.75, 1.5, 2.0]
    results = task_func(img_path, scale_factors)
    assert len(results) == len(scale_factors)
    for i, result in enumerate(results):
        assert isinstance(result, tuple)
        assert isinstance(result[0], plt.Axes)
        assert isinstance(result[1], np.ndarray)
        assert result[0].get_title() == f'Scale factor: {scale_factors[i]}'