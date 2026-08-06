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
    # Test case 1: Test with valid data
    data = [
        {'Name': 'John', 'Age': 25, 'Occupation': 'Engineer'},
        {'Name': 'Jane', 'Age': 30, 'Occupation': 'Doctor'},
        {'Name': 'Bob', 'Age': None, 'Occupation': 'Teacher'},
        {'Name': 'Alice', 'Age': 40, 'Occupation': 'Student'}
    ]
    expected_df = pd.DataFrame(data, columns=['Name', 'Age', 'Occupation'])
    actual_df = task_func(data)
    assert expected_df.equals(actual_df)

    # Test case 2: Test with missing data and fill_missing=True
    data = [
        {'Name': 'John', 'Age': 25, 'Occupation': 'Engineer'},
        {'Name': 'Jane', 'Age': 30, 'Occupation': 'Doctor'},
        {'Name': 'Bob', 'Age': None, 'Occupation': 'Teacher'},
        {'Name': 'Alice', 'Age': 40, 'Occupation': 'Student'}
    ]
    expected_df = pd.DataFrame(data, columns=['Name', 'Age', 'Occupation'])
    expected_df['Age'] = expected_df['Age'].fillna(0)
    expected_df['Age'] = expected_df['Age'].apply(lambda x: random.randint(0, 100) if pd.isnull(x) else x)
    actual_df = task_func(data, fill_missing=True)
    assert expected_df.equals(actual_df)

    # Test case 3: Test with missing data and fill_missing=False
    data = [
        {'Name': 'John', 'Age': 25, 'Occupation': 'Engineer'},
        {'Name': 'Jane', 'Age': 30, 'Occupation': 'Doctor'},
        {'Name': 'Bob', 'Age': None, 'Occupation': 'Teacher'},
        {'Name': 'Alice', 'Age': 40, 'Occupation': 'Student'}
    ]
    expected_df = pd.DataFrame(data, columns=['Name', 'Age', 'Occupation'])
    actual_df = task_func(data, fill_missing=False)
    assert expected_df.equals(actual_df)

    # Test case 4: Test with missing data and fill_missing=True and seed=123
    data = [
        {'Name': 'John', 'Age': 25, 'Occupation': 'Engineer'},
        {'Name': 'Jane', 'Age': 30, 'Occupation': 'Doctor'},
        {'Name': 'Bob', 'Age': None, 'Occupation': 'Teacher'},
        {'Name': 'Alice', 'Age': 40, 'Occupation': 'Student'}
    ]
    expected_df = pd.DataFrame(data, columns=['Name', 'Age', 'Occupation'])
    expected_df['Age'] = expected_df['Age'].fillna(0)
    expected_df['Age'] = expected_df['Age'].apply(lambda x: random.randint(0, 100) if pd.isnull(x) else x)
    actual_df = task_func(data, fill_missing=True, seed=123)
    assert expected_df.equals(actual_df)