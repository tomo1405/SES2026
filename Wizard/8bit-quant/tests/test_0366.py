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
        task_func(0, 'test.json')

    # Test case 2: n is greater than the number of words
    with pytest.raises(ValueError):
        task_func(10, 'test.json')

    # Test case 3: n is valid and file_name is valid
    n = 5
    file_name = 'test.json'
    task_func(n, file_name)

    # Test case 4: file_name is not a string
    with pytest.raises(TypeError):
        task_func(n, 123)

    # Test case 5: file_name is a valid string but does not end with .json
    with pytest.raises(ValueError):
        task_func(n, 'test')

    # Test case 6: file_name is a valid string and ends with .json
    file_name = 'test.json'
    task_func(n, file_name)

    # Test case 7: file_name is a valid string and ends with .json, but the file already exists
    with pytest.raises(FileExistsError):
        task_func(n, file_name)