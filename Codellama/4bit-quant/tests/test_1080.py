import pytest
from src_1080 import task_func

def test_task_func():
    data = [
        {"Price_String": "1000", "Price_Float": 1000.0},
        {"Price_String": "2000", "Price_Float": 2000.0},
        {"Price_String": "3000", "Price_Float": 3000.0},
        {"Price_String": "4000", "Price_Float": 4000.0},
        {"Price_String": "5000", "Price_Float": 5000.0},
    ]
    expected_mean = 3000.0
    expected_median = 3000.0
    expected_std_dev = 1000.0

    result, ax = task_func(data)

    assert result["mean"] == expected_mean
    assert result["median"] == expected_median
    assert result["std_dev"] == expected_std_dev
    assert ax.get_title() == "Histogram of Product Prices"
    assert ax.get_xlabel() == "Price"
    assert ax.get_ylabel() == "Frequency"