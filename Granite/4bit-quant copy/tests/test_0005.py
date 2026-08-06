import pytest
from collections import Counter
import itertools

def task_func(d):
    count_dict = Counter(itertools.chain.from_iterable(d.values()))
    return dict(count_dict)

def test_task_func():
    d = {'a': [1, 2, 3], 'b': [2, 3, 4], 'c': [3, 4, 5]}
    expected_output = {'1': 1, '2': 2, '3': 3, '4': 2, '5': 2}
    actual_output = task_func(d)
    assert actual_output == expected_output, "Output does not match expected output"

if __name__ == "__main__":
    pytest.main()