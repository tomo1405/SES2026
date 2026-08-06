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
    input_string = "Hello, World!\nHow are you?\nI'm doing well."
    file_paths = task_func(input_string)
    assert len(file_paths) == 3
    for filepath in file_paths:
        assert os.path.isfile(filepath)
        with open(filepath, 'r') as file:
            assert file.read() in input_string.split('\n')
        os.remove(filepath)

if __name__ == '__main__':
    test_task_func()