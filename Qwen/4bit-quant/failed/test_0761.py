import pytest
from src_0761 import task_func
import pandas as pd
import numpy as np

def test_task_func_default_parameters():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 100
    assert all(df['ID'].unique() == range(1, 101))
    assert all(df['Name'].isin(['Sopetón', 'Méndez', 'Gómez', 'Pérez', 'Muñoz', 'Smith', 'Johnson', 'Williams', 'Brown', 'Jones']))
    assert all(isinstance(dob, datetime.datetime) for dob in df['Date of Birth'])
    assert all(email.endswith('@example.com') for email in df['Email'])

def test_task_func_custom_parameters():
    df = task_func(start_year=2000, end_year=2010, email_domain='test.com', rng_seed=42)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 100
    assert all(df['ID'].unique() == range(1, 101))
    assert all(df['Name'].isin(['Sopetón', 'Méndez', 'Gómez', 'Pérez', 'Muñoz', 'Smith', 'Johnson', 'Williams', 'Brown', 'Jones']))
    assert all(2000 <= dob.year <= 2010 for dob in df['Date of Birth'])
    assert all(email.endswith('@test.com') for email in df['Email'])

def test_task_func_latin_names_encoding():
    df = task_func()
    assert all(isinstance(name, str) for name in df['Name'])

def test_task_func_email_format():
    df = task_func()
    for email in df['Email']:
        assert re.match(r'^[\w\.]+@[a-zA-Z]+\.[a-zA-Z]+$', email)

def test_task_func_rng_seed_reproducibility():
    df1 = task_func(rng_seed=42)
    df2 = task_func(rng_seed=42)
    assert df1.equals(df2)

def test_task_func_no_latin_names():
    df = task_func(latin_names=[])
    assert all(name not in ['Sopetón', 'Méndez', 'Gómez', 'Pérez', 'Muñoz'] for name in df['Name'])

def test_task_func_no_other_names():
    df = task_func(other_names=[])
    assert all(name not in ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones'] for name in df['Name'])