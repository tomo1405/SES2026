import pandas as pd
from src_0761 import task_func


def test_task_func():
    # Testing with default parameters
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 100
    assert list(df.columns) == ['ID', 'Name', 'Date of Birth', 'Email']
    assert all(df['ID'] == list(range(1, 101)))
    assert all(df['Name'].isin(['Sopetón', 'Méndez', 'Gómez', 'Pérez', 'Muñoz', 'Smith', 'Johnson', 'Williams', 'Brown', 'Jones']))
    assert all(df['Date of Birth'].dt.year.isin(list(range(1980, 2001))))
    assert all(df['Email'].str.endswith('example.com'))

    # Testing with custom parameters
    df = task_func(start_year=1990, end_year=2010, email_domain='test.com',
                   latin_names=['Sopetón', 'Méndez', 'Gómez', 'Pérez', 'Muñoz'],
                   other_names=['Smith', 'Johnson', 'Williams', 'Brown', 'Jones'],
                   rng_seed=42)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 100
    assert list(df.columns) == ['ID', 'Name', 'Date of Birth', 'Email']
    assert all(df['ID'] == list(range(1, 101)))
    assert all(df['Name'].isin(['Sopetón', 'Méndez', 'Gómez', 'Pérez', 'Muñoz', 'Smith', 'Johnson', 'Williams', 'Brown', 'Jones']))
    assert all(df['Date of Birth'].dt.year.isin(list(range(1990, 2011))))
    assert all(df['Email'].str.endswith('test.com'))