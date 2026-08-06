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
    # Test case 1: Test with an empty directory path
    json_dir_path = 'path/to/empty/directory'
    word_count = 10
    expected_result = []
    actual_result = task_func(json_dir_path, word_count)
    assert actual_result == expected_result

    # Test case 2: Test with a non-empty directory path
    json_dir_path = 'path/to/non-empty/directory'
    word_count = 5
    expected_result = [
        ('word1', 10),
        ('word2', 8),
        ('word3', 6),
        ('word4', 4),
        ('word5', 2)
    ]
    actual_result = task_func(json_dir_path, word_count)
    assert actual_result == expected_result

if __name__ == '__main__':
    pytest.main()