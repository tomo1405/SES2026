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
    # Test case 1: Test with no missing values
    data = [
        {'Name': 'John', 'Age': 30, 'Occupation': 'Engineer'},
        {'Name': 'Jane', 'Age': 25, 'Occupation': 'Doctor'},
        {'Name': 'Bob', 'Age': 40, 'Occupation': 'Teacher'}
    ]
    expected_df = pd.DataFrame(data, columns=['Name', 'Age', 'Occupation'])
    assert task_func(data).equals(expected_df)

    # Test case 2: Test with missing values
    data = [
        {'Name': 'John', 'Age': 30, 'Occupation': 'Engineer'},
        {'Name': 'Jane', 'Age': 25, 'Occupation': 'Doctor'},
        {'Name': 'Bob', 'Age': None, 'Occupation': 'Teacher'}
    ]
    expected_df = pd.DataFrame(data, columns=['Name', 'Age', 'Occupation'])
    assert task_func(data, fill_missing=True).equals(expected_df)

    # Test case 3: Test with custom seed
    data = [
        {'Name': 'John', 'Age': 30, 'Occupation': 'Engineer'},
        {'Name': 'Jane', 'Age': 25, 'Occupation': 'Doctor'},
        {'Name': 'Bob', 'Age': None, 'Occupation': 'Teacher'}
    ]
    expected_df = pd.DataFrame(data, columns=['Name', 'Age', 'Occupation'])
    assert task_func(data, fill_missing=True, seed=42).equals(expected_df)