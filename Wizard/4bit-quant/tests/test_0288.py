python
import os
import json
from collections import Counter

def test_task_func():
    directory = 'test_dir'
    os.makedirs(directory, exist_ok=True)
    with open(os.path.join(directory, 'file1.txt'), 'w') as f:
        f.write('hello world')
    with open(os.path.join(directory, 'file2.txt'), 'w') as f:
        f.write('goodbye world')
    with open(os.path.join(directory, 'file3.txt'), 'w') as f:
        f.write('hello goodbye')

    filename = 'word_counts.json'
    total_words = task_func(filename, directory)
    assert total_words == 6

    with open(filename, 'r') as f:
        word_counts = json.load(f)
    assert word_counts == {'hello': 2, 'world': 2, 'goodbye': 1}

    os.remove(os.path.join(directory, 'file1.txt'))
    os.remove(os.path.join(directory, 'file2.txt'))
    os.remove(os.path.join(directory, 'file3.txt'))
    os.rmdir(directory)