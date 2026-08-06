import pytest
from src_0008 import task_func
import os
import tempfile

def create_temp_csv(content):
    fd, path = tempfile.mkstemp()
    with os.fdopen(fd, 'w') as tmp:
        tmp.write(content)
    return path

def test_task_func():
    csv_content = """product,quantity
apple,10
banana,20
orange,15
banana,10
"""
    temp_csv_path = create_temp_csv(csv_content)
    try:
        result = task_func(temp_csv_path)
        assert result == "banana"
    finally:
        os.remove(temp_csv_path)

def test_task_func_with_tie():
    csv_content = """product,quantity
apple,10
banana,10
orange,15
"""
    temp_csv_path = create_temp_csv(csv_content)
    try:
        result = task_func(temp_csv_path)
        assert result == "orange"  # Assuming lexicographical order for tie-breaking
    finally:
        os.remove(temp_csv_path)

def test_task_func_single_entry():
    csv_content = """product,quantity
apple,10
"""
    temp_csv_path = create_temp_csv(csv_content)
    try:
        result = task_func(temp_csv_path)
        assert result == "apple"
    finally:
        os.remove(temp_csv_path)

def test_task_func_empty_file():
    csv_content = """product,quantity
"""
    temp_csv_path = create_temp_csv(csv_content)
    try:
        result = task_func(temp_csv_path)
        assert result is None  # Assuming None is returned for empty data
    finally:
        os.remove(temp_csv_path)