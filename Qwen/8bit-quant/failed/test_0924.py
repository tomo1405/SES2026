import pytest
from src_0924 import task_func

def test_task_func_insufficient_names():
    with pytest.raises(ValueError, match="Insufficient number of names or domains provided."):
        task_func([], ['example.com'])

def test_task_func_insufficient_domains():
    with pytest.raises(ValueError, match="Insufficient number of names or domains provided."):
        task_func(['Alice Smith'], [])

def test_task_func_default_num_records():
    df = task_func(['Alice Smith', 'Bob Johnson', 'Charlie Brown'], ['example.com'])
    assert len(df) == 5

def test_task_func_custom_num_records():
    df = task_func(['Alice Smith', 'Bob Johnson', 'Charlie Brown'], ['example.com'], num_records=3)
    assert len(df) == 3

def test_task_func_email_format():
    df = task_func(['Alice Smith', 'Bob Johnson', 'Charlie Brown'], ['example.com', 'test.com'], num_records=2)
    for email in df['Email']:
        assert re.match(r'^[a-z]+[at][a-z]+\.[a-z]+$', email)

def test_task_func_unique_emails():
    df = task_func(['Alice Smith', 'Bob Johnson', 'Charlie Brown'], ['example.com', 'test.com'], num_records=2)
    assert len(df['Email'].unique()) == 2

def test_task_func_name_email_mapping():
    df = task_func(['Alice Smith', 'Bob Johnson'], ['example.com'], num_records=2)
    for index, row in df.iterrows():
        name_part = row['Name'].split()[0].lower()
        email_part = row['Email'].split('[at]')[0]
        assert name_part == email_part