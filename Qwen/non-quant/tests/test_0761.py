import datetime
import re

import pandas as pd
from src_0761 import task_func


def test_task_func_default_parameters():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 100
    assert all(df['ID'].unique() == range(1, 101))
    assert all(isinstance(name, str) for name in df['Name'])
    assert all(isinstance(dob, datetime.datetime) for dob in df['Date of Birth'])
    assert all(email.endswith('@example.com') for email in df['Email'])

def test_task_func_custom_parameters():
    df = task_func(start_year=2000, end_year=2010, email_domain='test.com',
                   latin_names=['Álvarez', 'Rodríguez'], other_names=['Davis', 'Miller'], rng_seed=42)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 100
    assert all(df['ID'].unique() == range(1, 101))
    assert all(isinstance(name, str) for name in df['Name'])
    assert all(2000 <= dob.year <= 2010 for dob in df['Date of Birth'])
    assert all(email.endswith('@test.com') for email in df['Email'])

def test_task_func_rng_seed():
    df1 = task_func(rng_seed=42)
    df2 = task_func(rng_seed=42)
    assert df1.equals(df2)

def test_task_func_name_encoding():
    df = task_func()
    assert all(isinstance(name, str) for name in df['Name'])
    # Check for specific accented characters
    assert any('ó' in name for name in df['Name'])
    assert any('é' in name for name in df['Name'])
    assert any('ú' in name for name in df['Name'])

def test_task_func_email_format():
    df = task_func()
    for email in df['Email']:
        assert re.match(r'^[a-z.]+[0-9]+@example\.com$', email)