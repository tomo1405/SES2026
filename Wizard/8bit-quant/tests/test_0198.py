python
import heapq
import math
import matplotlib.pyplot as plt

def task_func(l1, l2, N=10):
    largest_diff_indices = heapq.nlargest(N, range(len(l1)), key=lambda i: abs(l1[i] - l2[i]))
    largest_diffs = [math.sqrt((l1[i] - l2[i])**2) for i in largest_diff_indices]

    fig, ax = plt.subplots()
    ax.plot(largest_diffs)

    return ax

# Test the function
def test_task_func():
    l1 = [1, 2, 3, 4, 5]
    l2 = [5, 4, 3, 2, 1]
    N = 2
    ax = task_func(l1, l2, N)
    assert ax.get_xlabel() == 'Index'
    assert ax.get_ylabel() == 'Distance'
    assert ax.get_title() == 'Largest Differences'
    assert ax.get_xticks() == [0, 1, 2, 3, 4]
    assert ax.get_xticklabels() == ['0', '1', '2', '3', '4']
    assert ax.get_yticks() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert ax.get_yticklabels() == ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    assert ax.lines[0].get_xdata().tolist() == [0, 1]
    assert ax.lines[0].get_ydata().tolist() == [1.4142135623730951, 1.7320508075688772]

test_task_func()