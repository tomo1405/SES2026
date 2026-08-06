import pytest
from src_0268 import task_func

@pytest.fixture
def input_data():
    return {'a': 1, 'b': 2, 'c': 3}

def test_task_func(input_data):
    fft, ax = task_func(input_data)
    assert fft is not None
    assert ax is not None

def test_task_func_with_sample_rate(input_data):
    fft, ax = task_func(input_data, sample_rate=44100)
    assert fft is not None
    assert ax is not None

def test_task_func_with_invalid_sample_rate(input_data):
    with pytest.raises(ValueError):
        task_func(input_data, sample_rate=-1)