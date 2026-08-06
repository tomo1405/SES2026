import numpy as np
import pytest
from src_0358 import task_func


def test_task_func_input_type():
    with pytest.raises(TypeError, match="x must be numpy.ndarray"):
        task_func([1, 2, 3])

def test_task_func_output_type():
    x = np.array([1, 2, 3])
    result = task_func(x)
    assert isinstance(result, np.ndarray)

def test_task_func_output_shape():
    x = np.array([1, 2, 3])
    result = task_func(x)
    assert result.shape == x.shape

def test_task_func_real_part():
    x = np.array([0, 1, 2])
    result = task_func(x)
    expected_real_part = norm.pdf(x, 0, 1)
    assert np.allclose(result.real, expected_real_part)

def test_task_func_imaginary_part():
    x = np.array([0, 1, 2])
    result = task_func(x)
    expected_imaginary_part = norm.pdf(x, 2, 2)
    assert np.allclose(result.imag, expected_imaginary_part)