python
import os
import json
import pandas as pd
from collections import Counter
import pytest

def task_func(json_dir_path, word_count):
    word_counter = Counter()
    
    for filename in os.listdir(json_dir_path):
        if filename.endswith('.json'):
            with open(os.path.join(json_dir_path, filename), 'r') as f:
                data = json.load(f)
                text = data.get('text', '')
                words = pd.Series(text.split())
                word_counter += Counter(words)
                
    return word_counter.most_common(word_count)

def test_task_func():
    json_dir_path = 'data'
    word_count = 10
    
    result = task_func(json_dir_path, word_count)
    
    assert len(result) == word_count
    assert all(isinstance(item, tuple) and len(item) == 2 for item in result)
    assert all(isinstance(item[0], str) and isinstance(item[1], int) for item in result)