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

    # Test case 5: List with 10 elements
    assert task_func(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']) == Counter({'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 1, 'G': 1, 'H': 1, 'I': 1, 'J': 1})

    # Test case 6: List with 100 elements
    l = ['A'] * 100
    random.shuffle(l)
    assert task_func(l) == Counter({'A': 100})