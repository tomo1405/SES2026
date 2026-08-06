import pytest
from src_0924 import task_func

def test_task_func_valid_input():
    person_names = ['John Doe', 'Jane Doe', 'John Smith']
    email_domains = ['example.com', 'example.org']
    num_records = 5

    df = task_func(person_names, email_domains, num_records)

    assert len(df) == num_records
    assert all(df['Name'].isin(person_names))
    assert all(df['Email'].str.contains('[at]'))
    assert all(df['Email'].str.endswith(email_domains))

def test_task_func_invalid_input():
    person_names = ['John Doe', 'Jane Doe', 'John Smith']
    email_domains = ['example.com', 'example.org']
    num_records = 5

    with pytest.raises(ValueError):
        task_func(person_names, [], num_records)

    with pytest.raises(ValueError):
        task_func([], email_domains, num_records)

    with pytest.raises(ValueError):
        task_func(person_names, email_domains, 0)