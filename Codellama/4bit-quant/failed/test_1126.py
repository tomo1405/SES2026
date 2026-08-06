import pytest
from src_1126 import task_func

def test_task_func():
    myString = 'https://www.example.com'
    token = 'your_token'
    expected_response = {'url': 'https://www.example.com'}
    response = task_func(myString, token)
    assert response == expected_response