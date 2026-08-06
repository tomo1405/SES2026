import pytest
from src_0722 import task_func
import os
import tempfile

def test_task_func_file_not_found():
    result = task_func("non_existent_file.csv")
    assert result is None

def test_task_func_empty_file():
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.close()
        result = task_func(temp_file.name)
        os.unlink(temp_file.name)
        assert result is None

def test_task_func_single_word():
    with tempfile.NamedTemporaryFile(delete=False, mode='w', newline='') as temp_file:
        writer = csv.writer(temp_file)
        writer.writerow(['hello'])
        temp_file.close()
        result = task_func(temp_file.name)
        os.unlink(temp_file.name)
        assert result == ('hello', 1)

def test_task_func_multiple_words():
    with tempfile.NamedTemporaryFile(delete=False, mode='w', newline='') as temp_file:
        writer = csv.writer(temp_file)
        writer.writerow(['hello', 'world'])
        writer.writerow(['hello', 'hello'])
        temp_file.close()
        result = task_func(temp_file.name)
        os.unlink(temp_file.name)
        assert result == ('hello', 3)

def test_task_func_tie_breaker():
    with tempfile.NamedTemporaryFile(delete=False, mode='w', newline='') as temp_file:
        writer = csv.writer(temp_file)
        writer.writerow(['apple', 'banana'])
        writer.writerow(['banana', 'apple'])
        temp_file.close()
        result = task_func(temp_file.name)
        os.unlink(temp_file.name)
        # Since the order of most common words is not guaranteed in case of a tie,
        # we check if the result is either ('apple', 2) or ('banana', 2)
        assert result in [('apple', 2), ('banana', 2)]