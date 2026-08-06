import pandas as pd
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import ast
import pytest

def task_func(db_file):
    conn = sqlite3.connect(db_file)
    df = pd.read_sql_query("SELECT * FROM EmailData", conn)
    df["list"] = df["list"].map(ast.literal_eval)
    df['sum'] = df['list'].apply(np.sum)
    df['mean'] = df['list'].apply(np.mean)
    df['var'] = df['list'].apply(np.var)

    ax = df[['sum', 'mean', 'var']].plot(kind='bar')
    plt.show()

    return df, ax

def test_task_func():
    db_file = "example.db"
    conn = sqlite3.connect(db_file)
    df = pd.read_sql_query("SELECT * FROM EmailData", conn)
    df["list"] = df["list"].map(ast.literal_eval)
    df['sum'] = df['list'].apply(np.sum)
    df['mean'] = df['list'].apply(np.mean)
    df['var'] = df['list'].apply(np.var)
    ax = df[['sum', 'mean', 'var']].plot(kind='bar')
    expected_return_value = (df, ax)
    actual_return_value = task_func(db_file)
    assert actual_return_value == expected_return_value