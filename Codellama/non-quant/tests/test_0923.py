import pytest
from src_0923 import task_func

def test_task_func():
    data = [
        {'text': 'This is a sample text'},
        {'text': 'This is another sample text'},
        {'text': 'This is a third sample text'}
    ]
    column = 'text'
    expected_output = [
        {'text': 'sample text'},
        {'text': 'sample text'},
        {'text': 'sample text'}
    ]
    output = task_func(data, column)
    assert output == expected_output