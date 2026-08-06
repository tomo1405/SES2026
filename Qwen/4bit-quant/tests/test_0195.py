import numpy as np
from src_0195 import task_func


def test_task_func():
    # Test with a small data size
    data_size = 10
    data, color = task_func(data_size)
    
    # Check if the data is of the correct type and size
    assert isinstance(data, np.ndarray)
    assert len(data) == data_size
    
    # Check if the color is one of the predefined colors
    assert color in BAR_COLOR
    
    # Test with a larger data size
    data_size = 100
    data, color = task_func(data_size)
    
    # Check if the data is of the correct type and size
    assert isinstance(data, np.ndarray)
    assert len(data) == data_size
    
    # Check if the color is one of the predefined colors
    assert color in BAR_COLOR
    
    # Test with a very large data size
    data_size = 1000
    data, color = task_func(data_size)
    
    # Check if the data is of the correct type and size
    assert isinstance(data, np.ndarray)
    assert len(data) == data_size
    
    # Check if the color is one of the predefined colors
    assert color in BAR_COLOR

def test_task_func_reproducibility():
    # Test reproducibility by checking if the same seed produces the same data
    data_size = 10
    data1, _ = task_func(data_size)
    data2, _ = task_func(data_size)
    
    assert np.array_equal(data1, data2)

def test_task_func_color_consistency():
    # Test if the color remains consistent for the same data size
    data_size = 10
    _, color1 = task_func(data_size)
    _, color2 = task_func(data_size)
    
    assert color1 == color2

def test_task_func_color_randomness():
    # Test if different data sizes produce different colors
    data_size1 = 10
    _, color1 = task_func(data_size1)
    
    data_size2 = 20
    _, color2 = task_func(data_size2)
    
    assert color1 != color2