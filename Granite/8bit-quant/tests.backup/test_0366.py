import pytest
from collections import Counter
import json
import random
from src_0366 import task_func

WORDS = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew']

def test_task_func_valid_input():
    n = 3
    file_name = 'test_file.json'
    seed = 77
    random.seed(seed)
    random.shuffle(WORDS)
    selected_words = WORDS[:n]
    counts = Counter(selected_words)
    with open(file_name, 'w') as f:
        json.dump(dict(counts), f)
    result = task_func(n, file_name, seed)
    assert result == file_name

def test_task_func_invalid_input():
    n = 10
    file_name = 'test_file.json'
    seed = 77
    random.seed(seed)
    random.shuffle(WORDS)
    selected_words = WORDS[:n]
    counts = Counter(selected_words)
    with open(file_name, 'w') as f:
        json.dump(dict(counts), f)
    with pytest.raises(ValueError):
        task_func(n, file_name, seed)

def test_task_func_invalid_file_name():
    n = 3
    file_name = 123
    seed = 77
    random.seed(seed)
    random.shuffle(WORDS)
    selected_words = WORDS[:n]
    counts = Counter(selected_words)
    with open(file_name, 'w') as f:
        json.dump(dict(counts), f)
    with pytest.raises(TypeError):
        task_func(n, file_name, seed)