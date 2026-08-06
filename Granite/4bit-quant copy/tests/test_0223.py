import pytest
from src_0223 import task_func

def test_task_func():
    # Test case 1: Test with a list of positive numbers
    list_input = [1, 3, 2, 4]
    expected_cumsum = [1, 4, 6, 10]
    expected_ax_title = "Cumulative Sum Plot"
    expected_ax_xlabel = "Index"
    expected_ax_ylabel = "Cumulative Sum"
    actual_cumsum, actual_ax = task_func(list_input)
    assert actual_cumsum == expected_cumsum
    assert actual_ax.get_title() == expected_ax_title
    assert actual_ax.get_xlabel() == expected_ax_xlabel
    assert actual_ax.get_ylabel() == expected_ax_ylabel

    # Test case 2: Test with a list of negative numbers
    list_input = [-2, -1, -3, -4]
    expected_cumsum = [-2, -3, -6, -10]
    expected_ax_title = "Cumulative Sum Plot"
    expected_ax_xlabel = "Index"
    expected_ax_ylabel = "Cumulative Sum"
    actual_cumsum, actual_ax = task_func(list_input)
    assert actual_cumsum == expected_cumsum
    assert actual_ax.get_title() == expected_ax_title
    assert actual_ax.get_xlabel() == expected_ax_xlabel
    assert actual_ax.get_ylabel() == expected_ax_ylabel

    # Test case 3: Test with a list of mixed numbers
    list_input = [1, -2, 3, -4, 5]
    expected_cumsum = [1, -1, 2, -1, 6]
    expected_ax_title = "Cumulative Sum Plot"
    expected_ax_xlabel = "Index"
    expected_ax_ylabel = "Cumulative Sum"
    actual_cumsum, actual_ax = task_func(list_input)
    assert actual_cumsum == expected_cumsum
    assert actual_ax.get_title() == expected_ax_title
    assert actual_ax.get_xlabel() == expected_ax_xlabel
    assert actual_ax.get_ylabel() == expected_ax_ylabel