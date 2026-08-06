python
import itertools
import statistics

def task_func(elements, subset_size):
    combinations = list(itertools.combinations(elements, subset_size))
    sums = [sum(combination) for combination in combinations]
    return {
        'mean': statistics.mean(sums),
        'median': statistics.median(sums),
        'mode': statistics.mode(sums)
    }

# Test the function with some sample inputs
def test_task_func():
    assert task_func([1, 2, 3, 4, 5], 2) == {'mean': 3.5, 'median': 3.5, 'mode': 3}
    assert task_func([1, 2, 3, 4, 5], 3) == {'mean': 3.0, 'median': 3.0, 'mode': 3}
    assert task_func([1, 2, 3, 4, 5], 4) == {'mean': 2.5, 'median': 2.5, 'mode': 2}
    assert task_func([1, 2, 3, 4, 5], 5) == {'mean': 2.0, 'median': 2.0, 'mode': 1}
    assert task_func([1, 2, 3, 4, 5], 6) == {'mean': 1.5, 'median': 2.0, 'mode': 1}
    assert task_func([1, 2, 3, 4, 5], 7) == {'mean': 1.0, 'median': 2.0, 'mode': 1}
    assert task_func([1, 2, 3, 4, 5], 8) == {'mean': 0.5, 'median': 2.0, 'mode': 1}
    assert task_func([1, 2, 3, 4, 5], 9) == {'mean': 0.0, 'median': 2.0, 'mode': 1}
    assert task_func([1, 2, 3, 4, 5], 10) == {'mean': 0.0, 'median': 2.0, 'mode': 1}

# Run the test function
test_task_func()