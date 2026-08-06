import pytest
from collections import Counter
import math

def task_func(nested_dict):
    counter = Counter()
    for sub_dict in nested_dict.values():
        counter.update(sub_dict)

    counter.pop('ele', None)

    return {k: math.sin(v) for k,v in counter.items()}

def test_task_func():
    nested_dict = {'a': {'x': 1, 'y': 2}, 'b': {'x': 3, 'y': 4, 'z': 5}}
    expected_result = {'x': 0.8414709848078965, 'y': 0.9092974268256817, 'z': 0.9589242746631385}
    result = task_func(nested_dict)
    assert result == expected_result

if __name__ == "__main__":
    pytest.main()