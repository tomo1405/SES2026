import pytest
from src_0919 import task_func
import pandas as pd

def test_task_func():
    data = [
        {'name': 'John Doe', 'age': 30},
        {'name': 'Jane Doe', 'age': 25},
        {'name': 'John Smith', 'age': 35},
        {'name': 'Jane Smith', 'age': 20}
    ]
    mapping = {'John': 'Johnny', 'Jane': 'Jenny'}
    expected_output = [
        {'name': 'Johnny Doe', 'age': 30},
        {'name': 'Jenny Doe', 'age': 25},
        {'name': 'Johnny Smith', 'age': 35},
        {'name': 'Jenny Smith', 'age': 20}
    ]
    output = task_func(data, mapping)
    assert output.equals(expected_output)