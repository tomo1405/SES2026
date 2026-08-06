python
import collections
import random
import string

def task_func(length=100):
    if length < 0:
        raise ValueError
    random_string = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=length))
    char_counts = collections.Counter(random_string)
    return dict(char_counts)

def test_task_func():
    # Test case 1: length is 100
    assert task_func(100) == {'A': 2, 'B': 2, 'C': 1, 'D': 1, 'E': 1, 'F': 1, 'G': 1, 'H': 1, 'I': 1, 'J': 1, 'K': 1, 'L': 1, 'M': 1, 'N': 1, 'O': 1, 'P': 1, 'Q': 1, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 1, 'W': 1, 'X': 1, 'Y': 1, 'Z': 1}

    # Test case 2: length is 0
    assert task_func(0) == {}

    # Test case 3: length is negative
    try:
        task_func(-1)
    except ValueError:
        assert True
    else:
        assert False

    # Test case 4: length is None
    try:
        task_func(None)
    except TypeError:
        assert True
    else:
        assert False