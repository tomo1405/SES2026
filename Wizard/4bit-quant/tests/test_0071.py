python
import pandas as pd
import json
import numpy as np
import pytest

# Constants
COLUMNS = ['email', 'list']

def task_func(json_file):
    with open(json_file, 'r') as file:
        email_data = json.load(file)
    if not email_data :
        return pd.DataFrame([], columns = COLUMNS + ["sum", "mean"]), None

    df = pd.DataFrame(email_data, columns=COLUMNS)
    df['sum'] = df['list'].apply(np.sum)
    df['mean'] = df['list'].apply(np.mean)

    ax = df[['sum', 'mean']].plot(kind='bar')

    return df, ax

def test_task_func():
    # Test case 1
    email_data = [{'email': 'user1', 'list': [1, 2, 3]}, {'email': 'user2', 'list': [4, 5, 6]}]
    df, ax = task_func(json_file='email_data.json')
    assert df.shape == (2, 3)
    assert df.columns.tolist() == COLUMNS + ["sum", "mean"]
    assert df['sum'].tolist() == [6, 15]
    assert df['mean'].tolist() == [2.0, 5.0]
    assert ax is not None

    # Test case 2
    email_data = []
    df, ax = task_func(json_file='email_data.json')
    assert df.shape == (0, 3)
    assert df.columns.tolist() == COLUMNS + ["sum", "mean"]
    assert ax is None

    # Test case 3
    email_data = None
    df, ax = task_func(json_file='email_data.json')
    assert df is None
    assert ax is None