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
    # Test case 1: n is 0
    assert task_func(0, 0.5) == ([], 0)

    # Test case 2: n is 1
    assert task_func(1, 0.5) == ([], 0)

    # Test case 3: n is 2
    assert task_func(2, 0.5) == ([0.5], 1)

    # Test case 4: n is 10
    numbers = [random.random() for _ in range(10)]
    avg = statistics.mean(numbers)
    greater_avg = [x for x in numbers if x > avg]
    num_greater_value = len(greater_avg)
    assert task_func(10, avg) == (greater_avg, num_greater_value)

    # Test case 5: n is 100
    numbers = [random.random() for _ in range(100)]
    avg = statistics.mean(numbers)
    greater_avg = [x for x in numbers if x > avg]
    num_greater_value = len(greater_avg)
    assert task_func(100, avg) == (greater_avg, num_greater_value)

    # Test case 6: n is 1000
    numbers = [random.random() for _ in range(1000)]
    avg = statistics.mean(numbers)
    greater_avg = [x for x in numbers if x > avg]
    num_greater_value = len(greater_avg)
    assert task_func(1000, avg) == (greater_avg, num_greater_value)