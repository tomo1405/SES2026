python
import random
import bisect
import statistics
import matplotlib.pyplot as plt
import pytest

def task_func(n, value):
    if n < 1:  # Handle case where n is 0 or less
        return [], 0

    numbers = [random.random() for _ in range(n)]
    avg = statistics.mean(numbers)
    greater_avg = [x for x in numbers if x > avg]

    numbers.sort()
    bpoint = bisect.bisect_right(numbers, value)
    num_greater_value = len(numbers) - bpoint

    plt.plot(numbers)
    plt.show()

    return greater_avg, num_greater_value

def test_task_func():
    # Test case 1: n=10, value=0.5
    n = 10
    value = 0.5
    greater_avg, num_greater_value = task_func(n, value)
    assert len(greater_avg) == 5
    assert num_greater_value == 5

    # Test case 2: n=0, value=0.5
    n = 0
    value = 0.5
    greater_avg, num_greater_value = task_func(n, value)
    assert len(greater_avg) == 0
    assert num_greater_value == 0

    # Test case 3: n=10, value=1.5
    n = 10
    value = 1.5
    greater_avg, num_greater_value = task_func(n, value)
    assert len(greater_avg) == 0
    assert num_greater_value == 0

    # Test case 4: n=10, value=0.2
    n = 10
    value = 0.2
    greater_avg, num_greater_value = task_func(n, value)
    assert len(greater_avg) == 8
    assert num_greater_value == 8

    # Test case 5: n=10, value=0.8
    n = 10
    value = 0.8
    greater_avg, num_greater_value = task_func(n, value)
    assert len(greater_avg) == 2
    assert num_greater_value == 2

    # Test case 6: n=1000000, value=0.5
    n = 1000000
    value = 0.5
    greater_avg, num_greater_value = task_func(n, value)
    assert len(greater_avg) == 500000
    assert num_greater_value == 500000

    # Test case 7: n=1000000, value=0.2
    n = 1000000
    value = 0.2
    greater_avg, num_greater_value = task_func(n, value)
    assert len(greater_avg) == 800000
    assert num_greater_value == 800000

    # Test case 8: n=1000000, value=0.8
    n = 1000000
    value = 0.8
    greater_avg, num_greater_value = task_func(n, value)
    assert len(greater_avg) == 200000
    assert num_greater_value == 200000