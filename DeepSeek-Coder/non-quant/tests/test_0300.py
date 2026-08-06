import pytest
from src_0300 import task_func

def test_task_func():
    # Test case 1: Basic functionality
    elements = [1, 2, 3, 4]
    subset_size = 2
    expected_product, expected_top_sums = 24, [7, 5]
    result_product, result_top_sums = task_func(elements, subset_size)
    assert result_product == expected_product
    assert result_top_sums == expected_top_sums

    # Add more test cases as needed

# Add more test cases as needed