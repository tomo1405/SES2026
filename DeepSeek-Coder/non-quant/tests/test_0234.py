import pytest
from src_0234 import task_func
import random
import matplotlib.pyplot as plt

# Sample data
class Object:
    value = 0
    def __init__(self, value=None):
        if value is None:
            self.value = random.gauss(0, 1)
        else:
            self.value = value

def test_task_func():
    # Create a list of Object instances
    obj_list = [Object() for _ in range(10)]
    attr = 'value'
    num_bins = 30
    seed = 0

    # Call the function
    ax = task_func(obj_list=obj_list, attr=attr, num_bins=num_bins, seed=seed)

    # Assertions to check the output
    assert ax is not None
    assert ax.get_title() == 'Histogram of attribute values'
    assert ax.get_xlabel() == 'Attribute Value'
    assert ax.get_ylabel() == 'Count'

    # Clean up
    plt.close()