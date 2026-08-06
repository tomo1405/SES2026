python
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
    # Test case 1
    json_dir_path = 'data'
    word_count = 10
    expected_result = [('the', 10), ('is', 8), ('and', 7), ('of', 6), ('to', 6), ('in', 5), ('a', 5), ('that', 4), ('it', 4), ('for', 3)]
    assert task_func(json_dir_path, word_count) == expected_result
    
    # Test case 2
    json_dir_path = 'data'
    word_count = 5
    expected_result = [('the', 10), ('is', 8), ('and', 7), ('of', 6), ('to', 6)]
    assert task_func(json_dir_path, word_count) == expected_result
    
    # Test case 3
    json_dir_path = 'data'
    word_count = 15
    expected_result = [('the', 10), ('is', 8), ('and', 7), ('of', 6), ('to', 6), ('in', 5), ('a', 5), ('that', 4), ('it', 4), ('for', 3), ('with', 2), ('on', 2), ('was', 2), ('as', 2), ('at', 2), ('by', 2), ('this', 1)]
    assert task_func(json_dir_path, word_count) == expected_result
    
    # Test case 4
    json_dir_path = 'data'
    word_count = 0
    expected_result = []
    assert task_func(json_dir_path, word_count) == expected_result
    
    # Test case 5
    json_dir_path = 'data'
    word_count = 20
    expected_result = [('the', 10), ('is', 8), ('and', 7), ('of', 6), ('to', 6), ('in', 5), ('a', 5), ('that', 4), ('it', 4), ('for', 3), ('with', 2), ('on', 2), ('was', 2), ('as', 2), ('at', 2), ('by', 2), ('this', 1), ('and', 1), ('was', 1), ('to', 1), ('for', 1), ('with', 1), ('that', 1), ('at', 1), ('by', 1), ('this', 1)]
    assert task_func(json_dir_path, word_count) == expected_result