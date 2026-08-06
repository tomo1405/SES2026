import pytest
from src_0876 import task_func
import pandas as pd
import numpy as np

def test_task_func_no_fill_missing():
    data = [
        {'Name': 'Alice', 'Age': 30, 'Occupation': 'Engineer'},
        {'Name': 'Bob', 'Age': np.nan, 'Occupation': 'Doctor'}
    ]
    df = task_func(data, fill_missing=False)
    assert df.equals(pd.DataFrame(data, columns=['Name', 'Age', 'Occupation']))

def test_task_func_fill_missing():
    data = [
        {'Name': 'Alice', 'Age': 30, 'Occupation': 'Engineer'},
        {'Name': 'Bob', 'Age': np.nan, 'Occupation': 'Doctor'}
    ]
    df = task_func(data, fill_missing=True, num_range=(20, 50))
    assert df['Age'].notnull().all()
    assert (df['Age'] >= 20).all() and (df['Age'] <= 50).all()

def test_task_func_custom_columns():
    data = [
        {'First': 'Alice', 'Second': 30, 'Third': 'Engineer'},
        {'First': 'Bob', 'Second': np.nan, 'Third': 'Doctor'}
    ]
    df = task_func(data, columns=['First', 'Second', 'Third'], fill_missing=True, num_range=(10, 40))
    assert df['Second'].notnull().all()
    assert (df['Second'] >= 10).all() and (df['Second'] <= 40).all()

def test_task_func_with_seed():
    data = [
        {'Name': 'Alice', 'Age': np.nan, 'Occupation': 'Engineer'},
        {'Name': 'Bob', 'Age': np.nan, 'Occupation': 'Doctor'}
    ]
    df1 = task_func(data, fill_missing=True, num_range=(0, 100), seed=42)
    df2 = task_func(data, fill_missing=True, num_range=(0, 100), seed=42)
    assert df1.equals(df2)

def test_task_func_empty_data():
    data = []
    df = task_func(data, fill_missing=True, num_range=(0, 100))
    assert df.empty