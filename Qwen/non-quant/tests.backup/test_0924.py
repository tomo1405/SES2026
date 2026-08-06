import pytest
from src_0924 import task_func
import pandas as pd

def test_task_func_insufficient_names():
    with pytest.raises(ValueError):
        task_func([], ['example.com'])

def test_task_func_insufficient_domains():
    with pytest.raises(ValueError):
        task_func(['John Doe'], [])

def test_task_func_default_num_records():
    df = task_func(['John Doe', 'Jane Smith', 'Alice Johnson'], ['example.com'])
    assert len(df) == 5

def test_task_func_custom_num_records():
    df = task_func(['John Doe', 'Jane Smith', 'Alice Johnson'], ['example.com'], num_records=3)
    assert len(df) == 3

def test_task_func_email_format():
    df = task_func(['John Doe'], ['example.com'])
    email = df.iloc[0]['Email']
    assert re.match(r'^john\[at\]example\.com$', email)

def test_task_func_unique_emails():
    df = task_func(['John Doe', 'Jane Smith', 'Alice Johnson'], ['example.com'], num_records=3)
    emails = df['Email'].tolist()
    assert len(emails) == len(set(emails))

def test_task_func_name_preservation():
    df = task_func(['John Doe', 'Jane Smith', 'Alice Johnson'], ['example.com'], num_records=3)
    names = df['Name'].tolist()
    assert all(name in ['John Doe', 'Jane Smith', 'Alice Johnson'] for name in names)