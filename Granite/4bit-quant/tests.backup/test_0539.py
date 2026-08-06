import sqlite3
import pandas as pd
import pytest

def task_func(db_name, table_name):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_name)

    # Dynamically get the first two numerical columns from the table (excluding 'id')
    df = pd.read_sql_query(f"SELECT * from {table_name}", conn)
    numerical_columns = df.select_dtypes(include=["float64", "int64"]).columns.tolist()
    if "id" in numerical_columns:
        numerical_columns.remove("id")
    if len(numerical_columns) < 2:
        raise ValueError("The table must have at least two numerical columns to plot.")

    # Plot the relationship between the two columns
    ax = df.plot.scatter(x=numerical_columns[0], y=numerical_columns[1])
    return ax

def test_task_func():
    db_name = "example.db"
    table_name = "example_table"
    numerical_columns = ["column1", "column2"]
    df = pd.DataFrame({
        "id": range(1, 101),
        "column1": range(101),
        "column2": range(101, 201)
    })
    df.to_sql(table_name, conn, if_exists="replace")
    ax = task_func(db_name, table_name)
    assert ax is not None
    assert ax.get_xlabel() == numerical_columns[0]
    assert ax.get_ylabel() == numerical_columns[1]