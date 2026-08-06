import pytest
from collections import Counter
import random
import string

# Constants
LETTERS = string.ascii_letters

def task_func(list_of_lists):
    flat_list = [random.choice(LETTERS) for _ in list_of_lists]
    return dict(Counter(flat_list))

def test_task_func():
    test_cases = [
        ([], {}),
        (["a"], {"a": 1}),
        (["a", "b", "c"], {"a": 1, "b": 1, "c": 1}),
        (["a", "a", "b", "c", "c"], {"a": 2, "b": 1, "c": 2}),
    ]

    for list_of_lists, expected_output in test_cases:
        actual_output = task_func(list_of_lists)
        assert actual_output == expected_output, f"Failed for input {list_of_lists}"

if __name__ == "__main__":
    pytest.main()