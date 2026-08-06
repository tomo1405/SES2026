import sqlite3
import pandas as pd
import csv
from io import StringIO
from src_0191 import task_func
import pytest

def test_task_func_with_stringio():
    csv_input = StringIO('Name,Age\nAlice,25\nBob,30')
    expected_dataframe = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [25, 30]})
    actual_dataframe = task_func(csv_input)
    assert actual_dataframe.equals(expected_dataframe)

def test_task_func_with_file_path():
    csv_input = 'test.csv'
    with open(csv_input, 'w') as f:
        f.write('Name,Age\nAlice,25\nBob,30')
    expected_dataframe = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [25, 30]})
    actual_dataframe = task_func(csv_input)
    assert actual_dataframe.equals(expected_dataframe)