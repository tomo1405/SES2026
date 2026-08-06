import matplotlib
from src_0234 import task_func


class TestTaskFunc:
    def test_task_func_returns_ax(self):
        obj_list = [Object(value=i) for i in range(10)]
        attr = 'value'
        num_bins = 30
        seed = 0
        ax = task_func(obj_list, attr, num_bins, seed)
        assert isinstance(ax, matplotlib.axes.Axes)

    def test_task_func_returns_ax_with_correct_title(self):
        obj_list = [Object(value=i) for i in range(10)]
        attr = 'value'
        num_bins = 30
        seed = 0
        ax = task_func(obj_list, attr, num_bins, seed)
        assert ax.get_title() == 'Histogram of attribute values'

    def test_task_func_returns_ax_with_correct_xlabel(self):
        obj_list = [Object(value=i) for i in range(10)]
        attr = 'value'
        num_bins = 30
        seed = 0
        ax = task_func(obj_list, attr, num_bins, seed)
        assert ax.get_xlabel() == 'Attribute Value'

    def test_task_func_returns_ax_with_correct_ylabel(self):
        obj_list = [Object(value=i) for i in range(10)]
        attr = 'value'
        num_bins = 30
        seed = 0
        ax = task_func(obj_list, attr, num_bins, seed)
        assert ax.get_ylabel() == 'Count'

    def test_task_func_returns_ax_with_correct_histogram(self):
        obj_list = [Object(value=i) for i in range(10)]
        attr = 'value'
        num_bins = 30
        seed = 0
        ax = task_func(obj_list, attr, num_bins, seed)
        assert ax.get_histogram() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]