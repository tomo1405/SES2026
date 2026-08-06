python
import os
import json
from collections import Counter

def test_task_func():
    directory = 'test_dir'
    filename = 'word_counts.json'
    os.makedirs(directory, exist_ok=True)
    with open(os.path.join(directory, 'file1.txt'), 'w') as file:
        file.write('hello world')
    with open(os.path.join(directory, 'file2.txt'), 'w') as file:
        file.write('hello python')
    with open(os.path.join(directory, 'file3.txt'), 'w') as file:
        file.write('python is awesome')
    with open(os.path.join(directory, 'file4.txt'), 'w') as file:
        file.write('hello')
    with open(os.path.join(directory, 'file5.txt'), 'w') as file:
        file.write('world')
    with open(os.path.join(directory, 'file6.txt'), 'w') as file:
        file.write('python')
    with open(os.path.join(directory, 'file7.txt'), 'w') as file:
        file.write('is')
    with open(os.path.join(directory, 'file8.txt'), 'w') as file:
        file.write('awesome')

    task_func(filename, directory)

    with open(filename, 'r') as file:
        word_counts = json.load(file)
    assert word_counts == {'hello': 2, 'world': 2, 'python': 2, 'is': 1, 'awesome': 1}

    os.remove(os.path.join(directory, 'file1.txt'))
    os.remove(os.path.join(directory, 'file2.txt'))
    os.remove(os.path.join(directory, 'file3.txt'))
    os.remove(os.path.join(directory, 'file4.txt'))
    os.remove(os.path.join(directory, 'file5.txt'))
    os.remove(os.path.join(directory, 'file6.txt'))
    os.remove(os.path.join(directory, 'file7.txt'))
    os.remove(os.path.join(directory, 'file8.txt'))
    os.rmdir(directory)