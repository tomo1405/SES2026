import pytest
from src_0234 import task_func
import random
import matplotlib.pyplot as plt

class TestTaskFunc:

    def test_task_func_with_default_parameters(self):
        # Create a list of objects with default values
        obj_list = [Object() for _ in range(100)]
        ax = task_func(obj_list, 'value')

        # Check if the returned object is an AxesSubplot
        assert isinstance(ax, plt.Axes)

    def test_task_func_with_custom_seed(self):
        # Create a list of objects with default values
        obj_list = [Object() for _ in range(100)]
        ax1 = task_func(obj_list, 'value', seed=42)
        ax2 = task_func(obj_list, 'value', seed=42)

        # Check if the histograms are the same with the same seed
        assert ax1.patches == ax2.patches

    def test_task_func_with_custom_attribute(self):
        # Create a list of objects with custom values
        obj_list = [Object(value=i) for i in range(10)]
        ax = task_func(obj_list, 'value')

        # Check if the returned object is an AxesSubplot
        assert isinstance(ax, plt.Axes)

    def test_task_func_with_custom_num_bins(self):
        # Create a list of objects with default values
        obj_list = [Object() for _ in range(100)]
        ax = task_func(obj_list, 'value', num_bins=10)

        # Check if the number of bins is correct
        assert len(ax.patches) == 10

    def test_task_func_with_empty_object_list(self):
        # Create an empty list of objects
        obj_list = []
        ax = task_func(obj_list, 'value')

        # Check if the returned object is an AxesSubplot
        assert isinstance(ax, plt.Axes)

    def test_task_func_with_nonexistent_attribute(self):
        # Create a list of objects with default values
        obj_list = [Object() for _ in range(100)]
        with pytest.raises(AttributeError):
            task_func(obj_list, 'nonexistent_attr')