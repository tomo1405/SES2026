import pytest
from collections import Counter
import json
import random
from src_0366 import task_func

WORDS = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew']

def test_task_func_valid_input():
    n = 3
    file_name = 'test_file.json'
    random.seed(77)
    random.shuffle(WORDS)
    selected_words = WORDS[:n]
    counts = Counter(selected_words)
    with open(file_name, 'w') as f:
        json.dump(dict(counts), f)
    result = task_func(n, file_name)
    assert result == file_name

def test_task_func_invalid_input():
    n = 10
    file_name = 'test_file.json'
    with pytest.raises(ValueError) as excinfo:
        task_func(n, file_name)
    assert 'n must be greater than 0' in str(excinfo.value)

def test_task_func_file_created():
    n = 3
    file_name = 'test_file.json'
    random.seed(77)
    random.shuffle(WORDS)
    selected_words = WORDS[:n]
    counts = Counter(selected_words)
    with open(file_name, 'w') as f:
        json.dump(dict(counts), f)
    task_func(n, file_name)
    assert os.path.exists(file_name)