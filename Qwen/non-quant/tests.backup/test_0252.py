import pytest
from src_0252 import task_func
import pandas as pd

def test_task_func_input_type():
    with pytest.raises(ValueError):
        task_func([1, 2, 3])

def test_task_func_empty_dataframe():
    df = pd.DataFrame(columns=['Job'])
    fig = task_func(df)
    assert isinstance(fig, plt.Figure)

def test_task_func_single_job():
    data = {'Job': ['Engineer']}
    df = pd.DataFrame(data)
    fig = task_func(df)
    assert isinstance(fig, plt.Figure)

def test_task_func_multiple_jobs():
    data = {'Job': ['Engineer', 'Doctor', 'Artist', 'Engineer']}
    df = pd.DataFrame(data)
    fig = task_func(df)
    assert isinstance(fig, plt.Figure)

def test_task_func_job_counts():
    data = {'Job': ['Engineer', 'Doctor', 'Artist', 'Engineer']}
    df = pd.DataFrame(data)
    fig = task_func(df)
    assert isinstance(fig, plt.Figure)