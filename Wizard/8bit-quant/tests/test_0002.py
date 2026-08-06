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
    assert task_func(100) == {'A': 2, 'B': 2, 'C': 2, 'D': 2, 'E': 2, 'F': 2, 'G': 2, 'H': 2, 'I': 2, 'J': 2, 'K': 2, 'L': 2, 'M': 2, 'N': 2, 'O': 2, 'P': 2, 'Q': 2, 'R': 2, 'S': 2, 'T': 2, 'U': 2, 'V': 2, 'W': 2, 'X': 2, 'Y': 2, 'Z': 2, 'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'f': 2, 'g': 2, 'h': 2, 'i': 2, 'j': 2, 'k': 2, 'l': 2, 'm': 2, 'n': 2, 'o': 2, 'p': 2, 'q': 2, 'r': 2, 's': 2, 't': 2, 'u': 2, 'v': 2, 'w': 2, 'x': 2, 'y': 2, 'z': 2}

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