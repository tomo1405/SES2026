import heapq
import math
import matplotlib.pyplot as plt
def task_func(l1, l2, N=10):
    largest_diff_indices = heapq.nlargest(N, range(len(l1)), key=lambda i: abs(l1[i] - l2[i]))
    largest_diffs = [math.sqrt((l1[i] - l2[i])**2) for i in largest_diff_indices]

    fig, ax = plt.subplots()
    ax.plot(largest_diffs)

    return ax