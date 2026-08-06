import heapq
import math
import matplotlib.pyplot as plt
import pytest

def task_func(l1, l2, N=10):
    largest_diff_indices = heapq.nlargest(N, range(len(l1)), key=lambda i: abs(l1[i] - l2[i]))
    largest_diffs = [math.sqrt((l1[i] - l2[i])**2) for i in largest_diff_indices]

    fig, ax = plt.subplots()
    ax.plot(largest_diffs)

    return ax

def test_task_func():
    l1 = [1, 2, 3, 4, 5]
    l2 = [2, 4, 6, 8, 10]
    N = 3
    expected_output = [1, 2, 3]  # This is just an example output, you should calculate it based on the input lists

    output = task_func(l1, l2, N)
    assert output == expected_output

if __name__ == "__main__":
    pytest.main()