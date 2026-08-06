import pandas as pd
import pytest
from src_0953 import task_func


def test_task_func_with_default_params():
    task_list = ["Task 1", "Task 2", "Task 3"]
    n_tasks = 2
    df = task_func(task_list, n_tasks)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == n_tasks
    assert all(col in df.columns for col in ["Task Name", "Assigned To", "Due Date"])

def test_task_func_with_custom_employees():
    task_list = ["Task 1", "Task 2", "Task 3"]
    n_tasks = 2
    employees = ["Alice", "Bob"]
    df = task_func(task_list, n_tasks, employees=employees)
    assert all(employee in employees for employee in df["Assigned To"])

def test_task_func_with_zero_tasks():
    task_list = ["Task 1", "Task 2", "Task 3"]
    n_tasks = 0
    df = task_func(task_list, n_tasks)
    assert df.empty

def test_task_func_with_more_tasks_than_available():
    task_list = ["Task 1"]
    n_tasks = 2
    df = task_func(task_list, n_tasks)
    assert len(df) == len(task_list)

def test_task_func_with_negative_tasks():
    task_list = ["Task 1", "Task 2", "Task 3"]
    n_tasks = -1
    with pytest.raises(ValueError):
        task_func(task_list, n_tasks)

def test_task_func_with_seed():
    task_list = ["Task 1", "Task 2", "Task 3"]
    n_tasks = 2
    seed = 42
    df1 = task_func(task_list, n_tasks, seed=seed)
    df2 = task_func(task_list, n_tasks, seed=seed)
    assert df1.equals(df2)

def test_task_func_with_empty_task_list():
    task_list = []
    n_tasks = 2
    df = task_func(task_list, n_tasks)
    assert df.empty