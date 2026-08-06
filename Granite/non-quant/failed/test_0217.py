import pandas as pd
import os
import json
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
    json_dir_path = 'path/to/json/files'
    word_count = 10
    expected_output = [
        ('word1', 100),
        ('word2', 80),
        ('word3', 60),
        # Add more expected output as needed
    ]
    
    actual_output = task_func(json_dir_path, word_count)
    
    assert actual_output == expected_output