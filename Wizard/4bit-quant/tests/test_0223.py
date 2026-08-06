python
import math
import numpy as np
import matplotlib.pyplot as plt
import pytest

def task_func(list_input):
    sorted_list = sorted(list_input, key=lambda x: (math.degrees(x), x))
    cumsum = np.cumsum(sorted_list)
    
    # Plotting the line chart
    ax = plt.plot(cumsum)[0].axes
    ax.set_title("Cumulative Sum Plot")
    ax.set_xlabel("Index")
    ax.set_ylabel("Cumulative Sum")
    
    return cumsum, ax

def test_task_func():
    # Test case 1
    list_input = [30, 40, 20, 10]
    expected_cumsum = [30, 70, 90, 100]
    expected_ax_title = "Cumulative Sum Plot"
    expected_ax_xlabel = "Index"
    expected_ax_ylabel = "Cumulative Sum"
    
    cumsum, ax = task_func(list_input)
    
    assert cumsum == expected_cumsum
    assert ax.get_title() == expected_ax_title
    assert ax.get_xlabel() == expected_ax_xlabel
    assert ax.get_ylabel() == expected_ax_ylabel
    
    # Test case 2
    list_input = [10, 20, 30, 40]
    expected_cumsum = [10, 30, 60, 100]
    expected_ax_title = "Cumulative Sum Plot"
    expected_ax_xlabel = "Index"
    expected_ax_ylabel = "Cumulative Sum"
    
    cumsum, ax = task_func(list_input)
    
    assert cumsum == expected_cumsum
    assert ax.get_title() == expected_ax_title
    assert ax.get_xlabel() == expected_ax_xlabel
    assert ax.get_ylabel() == expected_ax_ylabel