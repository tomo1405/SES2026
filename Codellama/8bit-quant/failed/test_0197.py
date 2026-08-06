import pytest
from src_0197 import task_func

def test_task_func():
    # Test case 1: length = 10, range_limit = 100, seed = 0
    ax, random_numbers = task_func(10, 100, 0)
    assert len(random_numbers) == 10
    assert all(random_numbers[i] <= 100 for i in range(10))
    assert all(random_numbers[i] >= 1 for i in range(10))
    assert ax.get_xlabel() == "Random Numbers"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == "Histogram of Random Numbers"

    # Test case 2: length = 10, range_limit = 100, seed = 1
    ax, random_numbers = task_func(10, 100, 1)
    assert len(random_numbers) == 10
    assert all(random_numbers[i] <= 100 for i in range(10))
    assert all(random_numbers[i] >= 1 for i in range(10))
    assert ax.get_xlabel() == "Random Numbers"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == "Histogram of Random Numbers"

    # Test case 3: length = 10, range_limit = 100, seed = 2
    ax, random_numbers = task_func(10, 100, 2)
    assert len(random_numbers) == 10
    assert all(random_numbers[i] <= 100 for i in range(10))
    assert all(random_numbers[i] >= 1 for i in range(10))
    assert ax.get_xlabel() == "Random Numbers"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == "Histogram of Random Numbers"

    # Test case 4: length = 10, range_limit = 100, seed = 3
    ax, random_numbers = task_func(10, 100, 3)
    assert len(random_numbers) == 10
    assert all(random_numbers[i] <= 100 for i in range(10))
    assert all(random_numbers[i] >= 1 for i in range(10))
    assert ax.get_xlabel() == "Random Numbers"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == "Histogram of Random Numbers"

    # Test case 5: length = 10, range_limit = 100, seed = 4
    ax, random_numbers = task_func(10, 100, 4)
    assert len(random_numbers) == 10
    assert all(random_numbers[i] <= 100 for i in range(10))
    assert all(random_numbers[i] >= 1 for i in range(10))
    assert ax.get_xlabel() == "Random Numbers"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == "Histogram of Random Numbers"

    # Test case 6: length = 10, range_limit = 100, seed = 5
    ax, random_numbers = task_func(10, 100, 5)
    assert len(random_numbers) == 10
    assert all(random_numbers[i] <= 100 for i in range(10))
    assert all(random_numbers[i] >= 1 for i in range(10))
    assert ax.get_xlabel() == "Random Numbers"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == "Histogram of Random Numbers"

    # Test case 7: length = 10, range_limit = 100, seed = 6
    ax, random_numbers = task_func(10, 100, 6)
    assert len(random_numbers) == 10
    assert all(random_numbers[i] <= 100 for i in range(10))
    assert all(random_numbers[i] >= 1 for i in range(10))
    assert ax.get_xlabel() == "Random Numbers"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == "Histogram of Random Numbers"

    # Test case 8: length = 10, range_limit = 100, seed = 7
    ax, random_numbers = task_func(10, 100, 7)
    assert len(random_numbers) == 10
    assert all(random_numbers[i] <= 100 for i in range(10))
    assert all(random_numbers[i] >= 1 for i in range(10))
    assert ax.get_xlabel() == "Random Numbers"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == "Histogram of Random Numbers"

    # Test case 9: length = 10, range_limit = 100, seed = 8
    ax, random_numbers = task_func(10, 100, 8)
    assert len(random_numbers) == 10
    assert all(random_numbers[i] <= 100 for i in range(10))
    assert all(random_numbers[i] >= 1 for i in range(10))
    assert ax.get_xlabel() == "Random Numbers"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == "Histogram of Random Numbers"

    # Test case 10: length = 10, range_limit = 100, seed = 9
    ax, random_numbers = task_func(10, 100, 9)
    assert len(random_numbers) == 10
    assert all(random_numbers[i] <= 100 for i in range(10))
    assert all(random_numbers[i] >= 1 for i in range(10))
    assert ax.get_xlabel() == "Random Numbers"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == "Histogram of Random Numbers"