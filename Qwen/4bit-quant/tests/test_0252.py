import matplotlib.pyplot as plt
import pandas as pd
import pytest
from src_0252 import task_func


def test_task_func_input_type():
    with pytest.raises(ValueError, match="Input df is not a DataFrame."):
        task_func([1, 2, 3])

def test_task_func_with_empty_dataframe():
    df = pd.DataFrame(columns=['Job'])
    fig = task_func(df)
    assert isinstance(fig, plt.Figure)

def test_task_func_with_data():
    data = {
        'Job': ['Engineer', 'Doctor', 'Engineer', 'Artist', 'Doctor', 'Artist', 'Artist']
    }
    df = pd.DataFrame(data)
    fig = task_func(df)
    assert isinstance(fig, plt.Figure)

def test_task_func_with_single_job():
    data = {
        'Job': ['Engineer'] * 10
    }
    df = pd.DataFrame(data)
    fig = task_func(df)
    assert isinstance(fig, plt.Figure)

def test_task_func_with_no_jobs():
    data = {
        'Job': []
    }
    df = pd.DataFrame(data)
    fig = task_func(df)
    assert isinstance(fig, plt.Figure)