import pytest
from src_0792 import task_func

def test_task_func():
    # Test case 1: Empty list
    assert task_func([]) == Counter()

    # Test case 2: List with 1 element
    assert task_func(['A']) == Counter({'A': 1})

    # Test case 3: List with 2 elements
    assert task_func(['A', 'B']) == Counter({'A': 1, 'B': 1})

    # Test case 4: List with 3 elements
    assert task_func(['A', 'B', 'C']) == Counter({'A': 1, 'B': 1, 'C': 1})

    # Test case 5: List with 4 elements
    assert task_func(['A', 'B', 'C', 'D']) == Counter({'A': 1, 'B': 1, 'C': 1, 'D': 1})

    # Test case 6: List with 5 elements
    assert task_func(['A', 'B', 'C', 'D', 'E']) == Counter({'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1})

    # Test case 7: List with 6 elements
    assert task_func(['A', 'B', 'C', 'D', 'E', 'F']) == Counter({'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 1})

    # Test case 8: List with 7 elements
    assert task_func(['A', 'B', 'C', 'D', 'E', 'F', 'G']) == Counter({'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 1, 'G': 1})

    # Test case 9: List with 8 elements
    assert task_func(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']) == Counter({'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 1, 'G': 1, 'H': 1})

    # Test case 10: List with 9 elements
    assert task_func(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']) == Counter({'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 1, 'G': 1, 'H': 1, 'I': 1})

    # Test case 11: List with 10 elements
    assert task_func(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']) == Counter({'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 1, 'G': 1, 'H': 1, 'I': 1, 'J': 1})