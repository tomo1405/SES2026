import pytest
from src_0761 import task_func
import pandas as pd
import numpy as np
import datetime

def test_task_func_default_parameters():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 100
    assert 'ID' in df.columns
    assert 'Name' in df.columns
    assert 'Date of Birth' in df.columns
    assert 'Email' in df.columns

def test_task_func_custom_parameters():
    df = task_func(start_year=2000, end_year=2010, email_domain='test.com',
                   latin_names=['Testé', 'Testá'], other_names=['Test'], rng_seed=42)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 100
    assert 'ID' in df.columns
    assert 'Name' in df.columns
    assert 'Date of Birth' in df.columns
    assert 'Email' in df.columns

    # Check specific values based on the seed
    assert df.iloc[0]['ID'] == 1
    assert df.iloc[0]['Name'] == 'Testá'
    assert isinstance(df.iloc[0]['Date of Birth'], datetime.datetime)
    assert df.iloc[0]['Email'] == 'testá2000@test.com'

def test_task_func_encoding():
    df = task_func()
    latin_names = ['Sopetón', 'Méndez', 'Gómez', 'Pérez', 'Muñoz']
    for name in latin_names:
        assert any(name in row['Name'] for _, row in df.iterrows())

def test_task_func_email_format():
    df = task_func()
    for index, row in df.iterrows():
        name_parts = row['Name'].lower().split()
        email = ''.join(name_parts) + str(row['Date of Birth'].year) + '@example.com'
        assert row['Email'] == email

def test_task_func_rng_seed():
    df1 = task_func(rng_seed=42)
    df2 = task_func(rng_seed=42)
    assert df1.equals(df2)