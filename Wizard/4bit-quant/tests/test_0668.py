python
import heapq
import collections

def task_func(x, n):
    counter = collections.Counter(x)
    most_frequent = heapq.nlargest(n, counter.keys(), key=counter.get)

    return most_frequent

def test_task_func():
    assert task_func([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3) == [1, 2, 3]
    assert task_func([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == [1, 2, 3, 4, 5]
    assert task_func([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert task_func([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1) == [1]
    assert task_func([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0) == []
    assert task_func([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 3) == [1, 1, 1]
    assert task_func([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 5) == [1, 1, 1, 1, 1]
    assert task_func([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 10) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert task_func([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1) == [1]
    assert task_func([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 0) == []