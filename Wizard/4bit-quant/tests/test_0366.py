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

def test_task_func():
    # Test case 1: n is less than 1
    with pytest.raises(ValueError):
        task_func(0, 'output.json')

    # Test case 2: n is greater than the length of WORDS
    with pytest.raises(ValueError):
        task_func(9, 'output.json')

    # Test case 3: n is valid
    n = 5
    file_name = 'output.json'
    task_func(n, file_name)
    with open(file_name, 'r') as f:
        data = json.load(f)
    assert len(data) == n
    for word in data:
        assert data[word] == 1