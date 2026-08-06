import pytest
from src_0234 import task_func, Object
import matplotlib.pyplot as plt
import numpy as np

@pytest.fixture
def setup_objects():
    return [Object(value=random.gauss(0, 1)) for _ in range(100)]

def test_task_func(setup_objects):
    ax = task_func(setup_objects, 'value', num_bins=10, seed=42)
    
    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes)
    
    # Check if the title and labels are set correctly
    assert ax.get_title() == 'Histogram of attribute values'
    assert ax.get_xlabel() == 'Attribute Value'
    assert ax.get_ylabel() == 'Count'
    
    # Check if the histogram data is correct
    attr_values = [obj.value for obj in setup_objects]
    _, bins, _ = ax.hist(attr_values, bins=10, alpha=0.5)
    expected_bins = np.histogram(attr_values, bins=10)[1]
    assert np.array_equal(bins, expected_bins)

def test_task_func_with_custom_values():
    custom_values = [1, 2, 3, 4, 5]
    obj_list = [Object(value=v) for v in custom_values]
    ax = task_func(obj_list, 'value', num_bins=5, seed=42)
    
    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes)
    
    # Check if the histogram data is correct
    attr_values = [obj.value for obj in obj_list]
    _, bins, _ = ax.hist(attr_values, bins=5, alpha=0.5)
    expected_bins = np.histogram(attr_values, bins=5)[1]
    assert np.array_equal(bins, expected_bins)