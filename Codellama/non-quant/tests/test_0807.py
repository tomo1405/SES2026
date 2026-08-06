from typing import Counter

from src_0807 import task_func


def test_task_func():
    # Test case 1: n = 2
    text = "This is a sample text for testing the task function."
    expected_output = Counter({('this', 'is'): 1, ('is', 'a'): 1, ('a', 'sample'): 1, ('sample', 'text'): 1, ('text', 'for'): 1, ('for', 'testing'): 1, ('testing', 'the'): 1, ('the', 'task'): 1, ('task', 'function'): 1})
    assert task_func(text, n=2) == expected_output

    # Test case 2: n = 3
    text = "This is a sample text for testing the task function."
    expected_output = Counter({('this', 'is', 'a'): 1, ('is', 'a', 'sample'): 1, ('a', 'sample', 'text'): 1, ('sample', 'text', 'for'): 1, ('text', 'for', 'testing'): 1, ('for', 'testing', 'the'): 1, ('testing', 'the', 'task'): 1, ('the', 'task', 'function'): 1})
    assert task_func(text, n=3) == expected_output

    # Test case 3: n = 4
    text = "This is a sample text for testing the task function."
    expected_output = Counter({('this', 'is', 'a', 'sample'): 1, ('is', 'a', 'sample', 'text'): 1, ('a', 'sample', 'text', 'for'): 1, ('sample', 'text', 'for', 'testing'): 1, ('text', 'for', 'testing', 'the'): 1, ('for', 'testing', 'the', 'task'): 1, ('testing', 'the', 'task', 'function'): 1})
    assert task_func(text, n=4) == expected_output