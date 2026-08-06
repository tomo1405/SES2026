from datetime import datetime

import matplotlib
import pytest
from src_0492 import task_func


def test_task_func():
    # Test that the function returns a tuple with two elements
    result = task_func(1000)
    assert len(result) == 2

    # Test that the first element of the tuple is a dictionary
    sales_data, ax = result
    assert isinstance(sales_data, dict)

    # Test that the second element of the tuple is a matplotlib Axes object
    assert isinstance(ax, matplotlib.axes.Axes)

    # Test that the function raises a ValueError when the start time is negative
    with pytest.raises(ValueError):
        task_func(-1000)

    # Test that the function raises a ValueError when the start date is after the current date
    with pytest.raises(ValueError):
        task_func(datetime.utcnow().timestamp() * 1000)

    # Test that the function returns a dictionary with the correct keys
    result = task_func(1000)
    assert set(result.keys()) == set(["Electronics", "Clothing", "Home", "Books", "Sports"])

    # Test that the function returns a dictionary with the correct values
    result = task_func(1000)
    assert all(isinstance(value, list) for value in result.values())
    assert all(len(value) == 10 for value in result.values())
    assert all(isinstance(item, int) for value in result.values() for item in value)
    assert all(item >= 10 and item <= 50 for value in result.values() for item in value)

    # Test that the function returns a matplotlib Axes object with the correct labels
    result = task_func(1000)
    ax = result[1]
    assert ax.get_xlabel() == "Days since 1970-01-01 00:00:00"
    assert ax.get_ylabel() == "Sales"
    assert ax.get_legend() == "Electronics"
    assert ax.get_legend() == "Clothing"
    assert ax.get_legend() == "Home"
    assert ax.get_legend() == "Books"
    assert ax.get_legend() == "Sports"

    # Test that the function returns a matplotlib Axes object with the correct plot
    result = task_func(1000)
    ax = result[1]
    assert ax.get_xlim() == (0, 10)
    assert ax.get_ylim() == (0, 50)
    assert ax.get_xticks() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert ax.get_yticks() == [10, 20, 30, 40, 50]
    assert ax.get_xticklabels() == ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    assert ax.get_yticklabels() == ["10", "20", "30", "40", "50"]