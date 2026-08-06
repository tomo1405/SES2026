import heapq
import collections
def task_func(x, n):
    counter = collections.Counter(x)
    most_frequent = heapq.nlargest(n, counter.keys(), key=counter.get)

    return most_frequent