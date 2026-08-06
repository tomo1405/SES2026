import pytest
from src_0924 import task_func

def test_task_func_insufficient_names():
    with pytest.raises(ValueError, match="Insufficient number of names or domains provided."):
        task_func([], ['example.com'])

def test_task_func_insufficient_domains():
    with pytest.raises(ValueError, match="Insufficient number of names or domains provided."):
        task_func(['John Doe'], [])

def test_task_func_default_records():
    person_names = ['Alice Smith', 'Bob Johnson', 'Charlie Brown']
    email_domains = ['example.com', 'test.org']
    df = task_func(person_names, email_domains)
    assert len(df) == 5
    assert all(df['Name'].isin(person_names))
    assert all(df['Email'].str.contains(r'\[at\]'))

def test_task_func_custom_records():
    person_names = ['Alice Smith', 'Bob Johnson', 'Charlie Brown', 'David Wilson']
    email_domains = ['example.com', 'test.org']
    df = task_func(person_names, email_domains, num_records=3)
    assert len(df) == 3
    assert all(df['Name'].isin(person_names))
    assert all(df['Email'].str.contains(r'\[at\]'))

def test_task_func_email_format():
    person_names = ['Alice Smith']
    email_domains = ['example.com']
    df = task_func(person_names, email_domains)
    email = df.iloc[0]['Email']
    assert re.match(r'^[a-z]+\[at\]example\.com$', email)