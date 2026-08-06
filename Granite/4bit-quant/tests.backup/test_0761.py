import pandas as pd
import numpy as np
import codecs
import re
import datetime
import pytest

from src_0761 import task_func

def test_task_func():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (100, 4)
    assert df.columns.tolist() == ['ID', 'Name', 'Date of Birth', 'Email']
    assert df['ID'].dtype == np.int64
    assert df['Name'].dtype == np.object
    assert df['Date of Birth'].dtype == np.object
    assert df['Email'].dtype == np.object

def test_task_func_with_custom_args():
    df = task_func(start_year=1900, end_year=2000, email_domain='example.com',
                   latin_names=['Foo', 'Bar'], other_names=['Baz', 'Qux'], rng_seed=42)
    assert df['ID'].iloc[0] == 1
    assert df['Name'].iloc[0] == 'Foo'
    assert df['Email'].iloc[0] == 'foo.1900@example.com'
    assert df['ID'].iloc[99] == 100
    assert df['Name'].iloc[99] == 'Qux'
    assert df['Email'].iloc[99] == 'qux.2000@example.com'

def test_task_func_with_invalid_args():
    with pytest.raises(ValueError):
        task_func(start_year=2000, end_year=1900)
    with pytest.raises(ValueError):
        task_func(email_domain='example')
    with pytest.raises(ValueError):
        task_func(latin_names=['Foo', 'Bar'], other_names=['Baz'])