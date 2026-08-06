python
import collections
import matplotlib.pyplot as plt
import pytest

def task_func(data):
    if not data:
        return dict(), None

    all_keys = set().union(*data)
    for d in data:
        for k, v in d.items():
            if v < 0:
                raise ValueError("Sales quantity must not be negative.")

    combined_dict = dict((k, [d.get(k, 0) for d in data]) for k in all_keys)
    total_sales = {k: sum(v) for k, v in combined_dict.items()}
    total_sales = dict(collections.OrderedDict(sorted(total_sales.items())))
    labels, values = zip(*total_sales.items())

    # Define colors dynamically to handle different numbers of fruit types
    colors = ["red", "yellow", "green", "blue", "purple"] * (len(labels) // 5 + 1)

    ax = plt.bar(labels, values, color=colors[: len(labels)])
    plt.xlabel("Fruit")
    plt.ylabel("Total Sales")
    plt.title("Total Fruit Sales")

    return total_sales, ax

def test_task_func():
    # Test case 1: Empty data
    data = []
    expected_total_sales = {}
    expected_ax = None
    actual_total_sales, actual_ax = task_func(data)
    assert actual_total_sales == expected_total_sales
    assert actual_ax == expected_ax

    # Test case 2: Valid data
    data = [
        {"apple": 10, "banana": 5},
        {"apple": 20, "orange": 15},
        {"banana": 10, "orange": 20},
    ]
    expected_total_sales = {"apple": 40, "banana": 25, "orange": 45}
    expected_ax = None
    actual_total_sales, actual_ax = task_func(data)
    assert actual_total_sales == expected_total_sales
    assert actual_ax == expected_ax

    # Test case 3: Invalid data
    data = [
        {"apple": 10, "banana": 5},
        {"apple": 20, "orange": -15},
        {"banana": 10, "orange": 20},
    ]
    with pytest.raises(ValueError):
        task_func(data)