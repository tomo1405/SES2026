import pandas as pd
import numpy as np
import codecs
import re
import datetime
from src_0761 import task_func

def test_task_func():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (100, 4)
    assert df.columns.tolist() == ['ID', 'Name', 'Date of Birth', 'Email']
    assert df['ID'].dtype == np.int64
    assert df['Name'].dtype == np.object
    assert df['Date of Birth'].dtype == 'datetime64[ns]'
    assert df['Email'].dtype == np.object

def test_task_func_with_custom_params():
    df = task_func(start_year=1990, end_year=2000, email_domain='example.com',
                   latin_names=['Foo', 'Bar'], other_names=['Baz', 'Qux'], rng_seed=42)
    assert df['ID'].iloc[0] == 1
    assert df['Name'].iloc[0] in ['Foo', 'Bar']
    assert df['Date of Birth'].iloc[0].year == 1990
    assert df['Email'].iloc[0].endswith('@example.com')