import re
import math
import pytest

def task_func(s):
    numbers = re.findall(r'\b\d+(?:\.\d+)?\b', s)  # Use non-capturing group for decimals
    count = len(numbers)
    sqrt_sum = sum(math.sqrt(float(num)) for num in numbers if num)  # Ensure conversion to float
    return count, sqrt_sum

def test_task_func():
    s = "There are 3 numbers: 1, 4.5, and 9."
    expected_count = 3
    expected_sqrt_sum = math.sqrt(1**2) + math.sqrt(4.5**2) + math.sqrt(9**2)
    actual_count, actual_sqrt_sum = task_func(s)
    assert actual_count == expected_count
    assert actual_sqrt_sum == expected_sqrt_sum

if __name__ == "__main__":
    pytest.main()