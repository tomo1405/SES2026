python
import pandas as pd
import random
import pytest

def task_func(data, columns=['Name', 'Age', 'Occupation'], fill_missing=False, num_range=(0, 100), seed=None):
    if seed is not None:
        random.seed(seed)

    df = pd.DataFrame(data, columns=columns)

    if fill_missing:
        for col in df.columns:
            if df[col].dtype in ['float64', 'int64']:
                df[col] = df[col].apply(lambda x: random.randint(*num_range) if pd.isnull(x) else x)

    return df

def test_task_func():
    data = [
        {'Name': 'John', 'Age': 25, 'Occupation': 'Engineer'},
        {'Name': 'Jane', 'Age': None, 'Occupation': 'Doctor'},
        {'Name': 'Bob', 'Age': 30, 'Occupation': 'Teacher'}
    ]

    expected_df = pd.DataFrame([
        {'Name': 'John', 'Age': 25, 'Occupation': 'Engineer'},
        {'Name': 'Jane', 'Age': 42, 'Occupation': 'Doctor'},
        {'Name': 'Bob', 'Age': 30, 'Occupation': 'Teacher'}
    ], columns=['Name', 'Age', 'Occupation'])

    df = task_func(data, fill_missing=True, num_range=(0, 100), seed=42)

    assert df.equals(expected_df)