import pytest
from src_0407 import task_func

@pytest.fixture
def setup():
    img_path = 'test_image.png'
    angle = 45
    return img_path, angle

def test_task_func(setup):
    img_path, angle = setup
    result = task_func(img_path, angle)
    assert isinstance(result, tuple), "The function should return a tuple."
    assert len(result) == 2, "The function should return a tuple with two elements."
    assert all(isinstance(arr, np.ndarray) for arr in result), "Both elements in the tuple should be numpy arrays."