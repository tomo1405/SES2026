import pytest
from src_0270 import task_func

def test_task_func():
    data_dict = {'a': 1, 'b': 2, 'c': 3}
    expected_dict = {'a': 1, 'b': 2, 'c': 3}
    expected_mean = 2
    expected_median = 2
    expected_mode = 1
    expected_ax_title = "Histogram of Normalized Values"
    expected_ax_xlabel = "Value"
    expected_ax_ylabel = "Frequency"

    returned_dict, returned_stats, returned_ax = task_func(data_dict)

    assert returned_dict == expected_dict
    assert returned_stats['mean'] == expected_mean
    assert returned_stats['median'] == expected_median
    assert returned_stats['mode'] == expected_mode
    assert returned_ax.get_title() == expected_ax_title
    assert returned_ax.get_xlabel() == expected_ax_xlabel
    assert returned_ax.get_ylabel() == expected_ax_ylabel