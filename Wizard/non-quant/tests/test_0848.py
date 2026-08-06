python
import re
import os
import string
import random
import pytest

def task_func(input_string, directory='./text_files'):
    lines = input_string.split('\n')
    file_paths = []
    for line in lines:
        line = re.sub('['+string.punctuation+']', '', line)
        filename = str(random.randint(10000, 99999)) + '.txt'
        filepath = os.path.join(directory, filename)
        file_paths.append(filepath)
        with open(filepath, 'w') as file:
            file.write(line)
    return file_paths

def test_task_func():
    input_string = "Hello, World!\nHow are you today?"
    file_paths = task_func(input_string)
    assert len(file_paths) == 2
    assert os.path.isfile(file_paths[0])
    assert os.path.isfile(file_paths[1])
    with open(file_paths[0], 'r') as file:
        assert file.read() == "Hello World"
    with open(file_paths[1], 'r') as file:
        assert file.read() == "How are you today"
    os.remove(file_paths[0])
    os.remove(file_paths[1])