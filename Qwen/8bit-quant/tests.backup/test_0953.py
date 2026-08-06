import pytest
from src_0953 import task_func
import pandas as pd
from datetime import datetime

def test_task_func_no_tasks():
    df = task_func([], 0)
    assert df.empty

def test_task_func_negative_tasks():
    with pytest.raises(ValueError):
        task_func(["Task 1"], -1)

def test_task_func_zero_tasks():
    df = task_func(["Task 1"], 0)
    assert df.empty

def test_task_func_more_tasks_than_available():
    df = task_func(["Task 1"], 10)
    assert len(df) == 1

def test_task_func_correct_columns():
    df = task_func(["Task 1"], 1)
    assert list(df.columns) == ["Task Name", "Assigned To", "Due Date"]

def test_task_func_correct_due_date_format():
    df = task_func(["Task 1"], 1)
    assert pd.to_datetime(df["Due Date"][0]).strftime("%Y-%m-%d") == datetime.today().strftime("%Y-%m-%d")

def test_task_func_with_seed():
    df1 = task_func(["Task 1", "Task 2"], 2, seed=42)
    df2 = task_func(["Task 1", "Task 2"], 2, seed=42)
    assert df1.equals(df2)

def test_task_func_task_name_format():
    df = task_func(["Task 1"], 1)
    assert "_" in df["Task Name"][0]

def test_task_func_employee_assignment():
    df = task_func(["Task 1"], 1)
    assert df["Assigned To"][0] in ["John Doe", "Jane Smith", "James Brown", "Mary Johnson", "Robert Davis"]

def test_task_func_multiple_tasks():
    df = task_func(["Task 1", "Task 2", "Task 3"], 3)
    assert len(df) == 3