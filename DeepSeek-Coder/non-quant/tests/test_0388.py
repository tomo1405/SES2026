import pytest
from src_0388 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    # Test case 1: Basic functionality
    city_dict = {'New York': 'New York', 'London': 'London', 'Beijing': 'Beijing'}
    result, _ = task_func(city_dict=city_dict)
    assert len(result) == 3
    assert all(isinstance(city, str) for city in result.keys())
    assert all(isinstance(pop, int) for pop in result.values())

    # Test case 2: Check for invalid max_range
    with pytest.raises(ValueError):
        task_func(city_dict={}, max_range=0)

    # Test case 3: Check plot generation
    city_dict = {'New York': 'New York', 'London': 'London', 'Beijing': 'Beijing'}
    result, _ = task_func(city_dict=city_dict)
    assert plt.gcf().get_axes() is not None

    # Clean up the plot to avoid affecting other tests
    plt.close()