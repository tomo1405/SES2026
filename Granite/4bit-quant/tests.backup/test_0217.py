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
    with pytest.raises(FileNotFoundError):
        task_func('', 10)

    # Test case 2: Test with a non-empty directory path
    test_dir_path = 'test_dir'
    os.makedirs(test_dir_path, exist_ok=True)
    test_json_path = os.path.join(test_dir_path, 'test.json')
    with open(test_json_path, 'w') as f:
        json.dump({'text': 'This is a test.'}, f)
    result = task_func(test_dir_path, 1)
    assert result == [('This', 1), ('is', 1), ('a', 1), ('test.', 1)]

    # Clean up
    os.rmdir(test_dir_path)

if __name__ == '__main__':
    test_task_func()