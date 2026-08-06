python
import pytest
from src_1109 import task_func

def test_task_func():
    result = [
        {'http://www.example.com': 10, 'https://www.example.com': 5},
        {'http://www.example.com': 15, 'https://www.example.com': 10},
        {'http://www.example.com': 20, 'https://www.example.com': 15},
        {'http://www.example.com': 25, 'https://www.example.com': 20},
        {'http://www.example.com': 30, 'https://www.example.com': 25},
        {'http://www.example.com': 35, 'https://www.example.com': 30},
        {'http://www.example.com': 40, 'https://www.example.com': 35},
        {'http://www.example.com': 45, 'https://www.example.com': 40},
        {'http://www.example.com': 50, 'https://www.example.com': 45},
        {'http://www.example.com': 55, 'https://www.example.com': 50},
        {'http://www.example.com': 60, 'https://www.example.com': 55},
        {'http://www.example.com': 65, 'https://www.example.com': 60},
        {'http://www.example.com': 70, 'https://www.example.com': 65},
        {'http://www.example.com': 75, 'https://www.example.com': 70},
        {'http://www.example.com': 80, 'https://www.example.com': 75},
        {'http://www.example.com': 85, 'https://www.example.com': 80},
        {'http://www.example.com': 90, 'https://www.example.com': 85},
        {'http://www.example.com': 95, 'https://www.example.com': 90},
        {'http://www.example.com': 100, 'https://www.example.com': 95},
    ]

    expected_output = {'http://www.example.com': 100, 'https://www.example.com': 100}

    assert task_func(result) == expected_output