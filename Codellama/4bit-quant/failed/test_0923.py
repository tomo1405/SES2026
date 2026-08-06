import pytest
from src_0923 import task_func

def test_task_func():
    data = [
        {'name': 'John Doe', 'age': 30},
        {'name': 'Jane Doe', 'age': 25},
        {'name': 'John Smith', 'age': 40}
    ]
    column = 'name'
    expected_output = [
        {'name': 'John Doe', 'age': 30},
        {'name': 'Jane Doe', 'age': 25},
        {'name': 'John Smith', 'age': 40}
    ]
    assert task_func(data, column) == expected_output

def test_task_func_with_stopwords():
    data = [
        {'name': 'John Doe', 'age': 30},
        {'name': 'Jane Doe', 'age': 25},
        {'name': 'John Smith', 'age': 40}
    ]
    column = 'name'
    expected_output = [
        {'name': 'John Doe', 'age': 30},
        {'name': 'Jane Doe', 'age': 25},
        {'name': 'John Smith', 'age': 40}
    ]
    assert task_func(data, column) == expected_output

def test_task_func_with_empty_data():
    data = []
    column = 'name'
    expected_output = []
    assert task_func(data, column) == expected_output

def test_task_func_with_empty_column():
    data = [
        {'name': 'John Doe', 'age': 30},
        {'name': 'Jane Doe', 'age': 25},
        {'name': 'John Smith', 'age': 40}
    ]
    column = ''
    expected_output = [
        {'name': 'John Doe', 'age': 30},
        {'name': 'Jane Doe', 'age': 25},
        {'name': 'John Smith', 'age': 40}
    ]
    assert task_func(data, column) == expected_output

def test_task_func_with_invalid_column():
    data = [
        {'name': 'John Doe', 'age': 30},
        {'name': 'Jane Doe', 'age': 25},
        {'name': 'John Smith', 'age': 40}
    ]
    column = 'invalid'
    expected_output = [
        {'name': 'John Doe', 'age': 30},
        {'name': 'Jane Doe', 'age': 25},
        {'name': 'John Smith', 'age': 40}
    ]
    assert task_func(data, column) == expected_output