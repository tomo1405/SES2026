import pytest
from src_1137 import task_func

def test_task_func():
    csv_path = task_func()
    assert csv_path == "emails.csv"

def test_task_func_with_custom_url():
    csv_path = task_func(url="https://example.com")
    assert csv_path == "emails.csv"

def test_task_func_with_custom_csv_path():
    csv_path = task_func(csv_path="custom_emails.csv")
    assert csv_path == "custom_emails.csv"

def test_task_func_with_custom_regex():
    csv_path = task_func(regex=r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b")
    assert csv_path == "emails.csv"

def test_task_func_with_custom_headers():
    csv_path = task_func(headers={'User-Agent': 'Custom User Agent'})
    assert csv_path == "emails.csv"