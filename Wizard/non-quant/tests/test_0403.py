python
import re
import requests
import json
import csv
import os

# Constants
API_URL = 'https://api.example.com/data'

def task_func(pattern):
    response = requests.get(API_URL)
    data = json.loads(response.text)
    matched_data = [re.findall(pattern, str(item)) for item in data['data']]
    with open('matched_data.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(matched_data)
    return os.path.abspath('matched_data.csv')

# Test cases
def test_task_func():
    # Test case 1
    pattern = r'\d+'
    expected_result = os.path.abspath('matched_data.csv')
    assert task_func(pattern) == expected_result

    # Test case 2
    pattern = r'\w+'
    expected_result = os.path.abspath('matched_data.csv')
    assert task_func(pattern) == expected_result

    # Test case 3
    pattern = r'\d+'
    expected_result = os.path.abspath('matched_data.csv')
    assert task_func(pattern) == expected_result

    # Test case 4
    pattern = r'\d+'
    expected_result = os.path.abspath('matched_data.csv')
    assert task_func(pattern) == expected_result

    # Test case 5
    pattern = r'\d+'
    expected_result = os.path.abspath('matched_data.csv')
    assert task_func(pattern) == expected_result

    # Test case 6
    pattern = r'\d+'
    expected_result = os.path.abspath('matched_data.csv')
    assert task_func(pattern) == expected_result

    # Test case 7
    pattern = r'\d+'
    expected_result = os.path.abspath('matched_data.csv')
    assert task_func(pattern) == expected_result

    # Test case 8
    pattern = r'\d+'
    expected_result = os.path.abspath('matched_data.csv')
    assert task_func(pattern) == expected_result

    # Test case 9
    pattern = r'\d+'
    expected_result = os.path.abspath('matched_data.csv')
    assert task_func(pattern) == expected_result

    # Test case 10
    pattern = r'\d+'
    expected_result = os.path.abspath('matched_data.csv')
    assert task_func(pattern) == expected_result