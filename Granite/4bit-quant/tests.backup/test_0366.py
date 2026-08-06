import pytest
from src_0366 import task_func
from collections import Counter
import json
import random

# Constants
WORDS = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew']

def test_task_func():
    n = 3
    file_name = 'test_file.json'
    seed = 77
    random.seed(seed)
    random.shuffle(WORDS)
    selected_words = WORDS[:n]
    expected_counts = Counter(selected_words)

    with open(file_name, 'w') as f:
        json.dump(dict(expected_counts), f)

    actual_file_name = task_func(n, file_name, seed)

    with open(actual_file_name, 'r') as f:
        actual_counts = json.load(f)

    assert actual_counts == dict(expected_counts)

def test_task_func_invalid_n():
    n = -1
    file_name = 'test_file.json'
    seed = 77

    with pytest.raises(ValueError) as e:
        task_func(n, file_name, seed)

    assert str(e.value) == 'n must be greater than 0'