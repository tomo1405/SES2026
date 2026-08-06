python
import random
from collections import Counter
from itertools import cycle

# Constants
ELEMENTS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

def task_func(l):
    if not l:  # Check if the list is empty
        return Counter()  # Return an empty counter if the list is empty

    random.shuffle(l)
    l_cycled = cycle(l)
    counter = Counter(next(l_cycled) for _ in range(30))
    keys = list(counter.keys())
    counter = Counter({k: counter[k] for k in keys[3:] + keys[:3]})
    
    return counter

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

    # Test case 12: List with 10 elements shuffled
    assert task_func(['J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']) == Counter({'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 1, 'G': 1, 'H': 1, 'I': 1, 'J': 1})

    # Test case 13: List with 10 elements shuffled and repeated
    assert task_func(['J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']) == Counter({'A': 2, 'B': 2, 'C': 2, 'D': 2, 'E': 2, 'F': 2, 'G': 2, 'H': 2, 'I': 2, 'J': 2})