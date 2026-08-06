import pandas as pd
import random
import re
from src_0924 import task_func
import pytest

def test_task_func():
    person_names = ['John Smith', 'Jane Doe', 'Bob Johnson']
    email_domains = ['gmail.com', 'yahoo.com', 'outlook.com']
    num_records = 2

    df = task_func(person_names, email_domains, num_records)

    assert isinstance(df, pd.DataFrame)
    assert df.shape == (num_records, 2)
    assert df.columns.tolist() == ['Name', 'Email']
    for index, row in df.iterrows():
        name, email = row
        assert name in person_names
        assert re.match(r'[^@]+@[^@]+\.[^@]+', email)

def test_task_func_invalid_input():
    person_names = ['John Smith']
    email_domains = []
    num_records = 5

    with pytest.raises(ValueError) as exc_info:
        task_func(person_names, email_domains, num_records)

    assert str(exc_info.value) == "Insufficient number of names or domains provided."