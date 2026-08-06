import json
import csv
import requests
from io import StringIO
from src_1119 import task_func
import pytest

# Constants
CSV_URL = 'https://example.com/data.csv'
JSON_FILE = 'data.json'

def test_task_func():
    response = requests.get(CSV_URL)
    csv_data = csv.reader(StringIO(response.text))

    headers = next(csv_data)
    json_data = [dict(zip(headers, row)) for row in csv_data]

    with open(JSON_FILE, 'w') as json_file:
        json.dump(json_data, json_file)

    assert task_func() == JSON_FILE

def test_task_func_with_custom_csv_url():
    custom_csv_url = 'https://example.com/custom_data.csv'
    response = requests.get(custom_csv_url)
    csv_data = csv.reader(StringIO(response.text))

    headers = next(csv_data)
    json_data = [dict(zip(headers, row)) for row in csv_data]

    with open(JSON_FILE, 'w') as json_file:
        json.dump(json_data, json_file)

    assert task_func(csv_url=custom_csv_url) == JSON_FILE

def test_task_func_with_custom_json_file_path():
    custom_json_file_path = 'custom_data.json'
    response = requests.get(CSV_URL)
    csv_data = csv.reader(StringIO(response.text))

    headers = next(csv_data)
    json_data = [dict(zip(headers, row)) for row in csv_data]

    with open(custom_json_file_path, 'w') as json_file:
        json.dump(json_data, json_file)

    assert task_func(json_file_path=custom_json_file_path) == custom_json_file_path