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
    db_file = "test_db.db"
    conn = sqlite3.connect(db_file)
    df = pd.DataFrame({"list": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]})
    df.to_sql("EmailData", conn, index=False)
    conn.close()

    df, ax = task_func(db_file)

    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)

    expected_columns = ["sum", "mean", "var"]
    assert all(column in df.columns for column in expected_columns)

    expected_values = {"sum": [6, 15, 24], "mean": [2.0, 5.0, 8.0], "var": [1.0, 1.0, 1.0]}
    for column, values in expected_values.items():
        assert all(df[column].round(1) == value for value in values)

    plt.close()

if __name__ == "__main__":
    pytest.main()