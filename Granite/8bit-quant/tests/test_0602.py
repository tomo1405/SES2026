import pandas as pd
import seaborn as sns
import time
import pytest
from src_0602 import task_func

@pytest.fixture
def df():
    return pd.DataFrame({'Word': ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']})

def test_task_func_valid_input(df):
    assert task_func(df, 'B') is not None

def test_task_func_invalid_input(df):
    with pytest.raises(ValueError):
        task_func(df, 'Z')

def test_task_func_empty_df(df):
    df = pd.DataFrame()
    assert task_func(df, 'A') is None

def test_task_func_no_match(df):
    assert task_func(df, 'Z') is None

def test_task_func_boxplot_title(df):
    ax = task_func(df, 'B')
    assert ax.get_title() == "Word Lengths Distribution for Words Starting with 'B'"

def test_task_func_timing(df):
    start_time = time.time()
    task_func(df, 'B')
    end_time = time.time()
    assert start_time < end_time