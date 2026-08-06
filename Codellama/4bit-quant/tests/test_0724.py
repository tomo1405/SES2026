import csv
import os

from src_0724 import task_func


def test_task_func():
    url = 'https://www.example.com'
    csv_file_path = task_func(url)
    assert os.path.exists(csv_file_path)
    with open(csv_file_path, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
        assert len(data) > 0
        assert len(data[0]) > 0

def test_task_func_with_invalid_url():
    url = 'https://www.example.com/invalid'
    csv_file_path = task_func(url)
    assert csv_file_path is None

def test_task_func_with_invalid_table():
    url = 'https://www.example.com'
    with open(CSV_FILE_PATH, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['test', 'test'])
    csv_file_path = task_func(url)
    assert csv_file_path is None