import pytest
from src_0924 import task_func

def test_task_func_valid_input():
    person_names = ['John Doe', 'Jane Doe', 'Bob Smith']
    email_domains = ['example.com', 'example.org']
    num_records = 2

    df = task_func(person_names, email_domains, num_records)

    assert len(df) == num_records
    assert all(df['Name'].isin(person_names[:num_records]))
    assert all(df['Email'].str.contains('[at]'))

def test_task_func_invalid_input():
    person_names = ['John Doe', 'Jane Doe', 'Bob Smith']
    email_domains = ['example.com', 'example.org']
    num_records = 5

    with pytest.raises(ValueError):
        task_func(person_names, email_domains, num_records)