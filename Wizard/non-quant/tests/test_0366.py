python
import json
import random
from collections import Counter

# Constants
WORDS = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew']

def task_func(n, file_name, seed=77):
    random.seed(seed)
    if n < 1 or n > len(WORDS):
        raise ValueError('n must be greater than 0')
    random.shuffle(WORDS)
    selected_words = WORDS[:n]
    counts = Counter(selected_words)

    with open(file_name, 'w') as f:
        json.dump(dict(counts), f)

    return file_name

# Test the function
def test_task_func():
    # Test case 1
    n = 3
    file_name = 'test.json'
    result = task_func(n, file_name)
    assert result == file_name
    with open(file_name, 'r') as f:
        data = json.load(f)
    assert data == {'apple': 1, 'banana': 1, 'cherry': 1}
    # Test case 2
    n = 5
    file_name = 'test2.json'
    result = task_func(n, file_name)
    assert result == file_name
    with open(file_name, 'r') as f:
        data = json.load(f)
    assert data == {'apple': 1, 'banana': 1, 'cherry': 1, 'date': 1, 'elderberry': 1}
    # Test case 3
    n = 0
    file_name = 'test3.json'
    try:
        result = task_func(n, file_name)
    except ValueError as e:
        assert str(e) == 'n must be greater than 0'
    else:
        assert False, 'Expected ValueError'
    # Test case 4
    n = 9
    file_name = 'test4.json'
    try:
        result = task_func(n, file_name)
    except ValueError as e:
        assert str(e) == 'n must be greater than 0'
    else:
        assert False, 'Expected ValueError'
    # Test case 5
    n = 3
    file_name = 'test5.json'
    result = task_func(n, file_name, seed=123)
    assert result == file_name
    with open(file_name, 'r') as f:
        data = json.load(f)
    assert data == {'apple': 1, 'banana': 1, 'cherry': 1}
    # Test case 6
    n = 5
    file_name = 'test6.json'
    result = task_func(n, file_name, seed=123)
    assert result == file_name
    with open(file_name, 'r') as f:
        data = json.load(f)
    assert data == {'apple': 1, 'banana': 1, 'cherry': 1, 'date': 1, 'elderberry': 1}
    # Test case 7
    n = 0
    file_name = 'test7.json'
    try:
        result = task_func(n, file_name, seed=123)
    except ValueError as e:
        assert str(e) == 'n must be greater than 0'
    else:
        assert False, 'Expected ValueError'
    # Test case 8
    n = 9
    file_name = 'test8.json'
    try:
        result = task_func(n, file_name, seed=123)
    except ValueError as e:
        assert str(e) == 'n must be greater than 0'
    else:
        assert False, 'Expected ValueError'

test_task_func()