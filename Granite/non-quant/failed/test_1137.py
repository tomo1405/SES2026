import pytest
from src_1137 import task_func

def test_task_func():
    csv_path = task_func()
    with open(csv_path, 'r', newline='') as f:
        reader = csv.reader(f)
        rows = list(reader)
        assert rows[0] == ['Emails']
        assert len(rows) > 1

def test_task_func_with_custom_url():
    csv_path = task_func(url="https://example.com")
    with open(csv_path, 'r', newline='') as f:
        reader = csv.reader(f)
        rows = list(reader)
        assert rows[0] == ['Emails']
        assert len(rows) > 1

def test_task_func_with_custom_csv_path():
    csv_path = task_func(csv_path="custom_emails.csv")
    with open(csv_path, 'r', newline='') as f:
        reader = csv.reader(f)
        rows = list(reader)
        assert rows[0] == ['Emails']
        assert len(rows) > 1

def test_task_func_with_custom_regex():
    csv_path = task_func(regex=r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b")
    with open(csv_path, 'r', newline='') as f:
        reader = csv.reader(f)
        rows = list(reader)
        assert rows[0] == ['Emails']
        assert len(rows) > 1

def test_task_func_with_custom_headers():
    csv_path = task_func(headers={'User-Agent': 'Custom'})
    with open(csv_path, 'r', newline='') as f:
        reader = csv.reader(f)
        rows = list(reader)
        assert rows[0] == ['Emails']
        assert len(rows) > 1