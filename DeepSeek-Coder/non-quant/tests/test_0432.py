import pytest
from src_0432 import task_func
import numpy as np
import os

@pytest.fixture
def setup():
    # Create a temporary image file for testing
    with open('test_image.png', 'w') as f:
        f.write('test')
    yield
    os.remove('test_image.png')

def test_task_func(setup):
    result = task_func('test_image.png')
    assert isinstance(result, np.ndarray)
    assert result.shape == (256,)