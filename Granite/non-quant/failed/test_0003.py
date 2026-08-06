import random
import statistics
from src_0003 import task_func

def test_task_func():
    # Test case 1: an empty dictionary
    assert task_func([]) == {}

    # Test case 2: a dictionary with one key-value pair
    assert task_func(['A']) == {'A': [random.randint(0, 100)]}

    # Test case 3: a dictionary with multiple key-value pairs
    num_keys = 5
    num_values = 10
    letters = [chr(ord('A') + i) for i in range(num_keys)]
    random_dict = {k: [random.randint(0, 100) for _ in range(num_values)] for k in letters}
    sorted_dict = dict(sorted(random_dict.items(), key=lambda item: statistics.mean(item[1]), reverse=True))
    assert task_func(letters) == sorted_dict