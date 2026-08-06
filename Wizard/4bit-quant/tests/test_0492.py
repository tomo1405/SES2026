python
import random
from datetime import datetime
import matplotlib.pyplot as plt
import pytest

def task_func(epoch_milliseconds, seed=None):
    CATEGORIES = ["Electronics", "Clothing", "Home", "Books", "Sports"]

    if seed is not None:
        random.seed(seed)

    if epoch_milliseconds < 0:
        raise ValueError("Start time cannot be negative.")

    start_time = datetime.utcfromtimestamp(epoch_milliseconds / 1000.0)
    current_time = datetime.utcnow()
    days_diff = (current_time - start_time).days
    if days_diff <= 0:
        raise ValueError("Start date must be before current time.")

    sales_data = {category: [0] * days_diff for category in CATEGORIES}

    for i in range(days_diff):
        for category in CATEGORIES:
            sales = random.randint(10, 50)
            sales_data[category][i] += sales

    fig, ax = plt.subplots()
    for category, sales in sales_data.items():
        ax.plot(range(days_diff), sales, label=category)

    ax.set_xlabel("Days since " + start_time.strftime("%Y-%m-%d %H:%M:%S"))
    ax.set_ylabel("Sales")
    ax.legend()

    return sales_data, ax

def test_task_func():
    # Test case 1: valid input
    sales_data, ax = task_func(1622505600000, seed=42)
    assert len(sales_data) == 5
    assert len(sales_data["Electronics"]) == 31
    assert len(sales_data["Clothing"]) == 31
    assert len(sales_data["Home"]) == 31
    assert len(sales_data["Books"]) == 31
    assert len(sales_data["Sports"]) == 31
    assert ax.get_xlabel() == "Days since 2021-05-20 00:00:00"
    assert ax.get_ylabel() == "Sales"
    assert ax.get_legend_handles_labels()[1] == ("Electronics", "Clothing", "Home", "Books", "Sports")

    # Test case 2: invalid input (start time cannot be negative)
    with pytest.raises(ValueError):
        task_func(-1)

    # Test case 3: invalid input (start date must be before current time)
    with pytest.raises(ValueError):
        task_func(1622505600000)