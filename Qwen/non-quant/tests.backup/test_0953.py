import pytest
from src_0953 import task_func
import pandas as pd
import random
from datetime import datetime

def test_task_func_no_tasks():
    result = task_func([], 0)
    assert result.empty

def test_task_func_no_employees():
    with pytest.raises(ValueError):
        task_func(["Task 1"], 1, employees=[])

def test_task_func_negative_n_tasks():
    with pytest.raises(ValueError):
        task_func(["Task 1"], -1)

def test_task_func_single_task():
    random.seed(0)
    result = task_func(["Task 1"], 1)
    expected_columns = ["Task Name", "Assigned To", "Due Date"]
    assert list(result.columns) == expected_columns
    assert len(result) == 1
    assert result.iloc[0]["Task Name"] == "Task_1"
    assert result.iloc[0]["Assigned To"] in ["John Doe", "Jane Smith", "James Brown", "Mary Johnson", "Robert Davis"]
    assert result.iloc[0]["Due Date"] == datetime.today().strftime("%Y-%m-%d")

def test_task_func_multiple_tasks():
    random.seed(0)
    result = task_func(["Task 1", "Task 2", "Task 3"], 3)
    expected_columns = ["Task Name", "Assigned To", "Due Date"]
    assert list(result.columns) == expected_columns
    assert len(result) == 3
    assert result.iloc[0]["Task Name"] == "Task_1"
    assert result.iloc[1]["Task Name"] == "Task_2"
    assert result.iloc[2]["Task Name"] == "Task_3"
    for row in result.itertuples(index=False):
        assert row["Assigned To"] in ["John Doe", "Jane Smith", "James Brown", "Mary Johnson", "Robert Davis"]
        assert row["Due Date"] == datetime.today().strftime("%Y-%m-%d")

def test_task_func_more_tasks_than_available():
    random.seed(0)
    result = task_func(["Task 1"], 2)
    assert len(result) == 1
    assert result.iloc[0]["Task Name"] == "Task_1"

def test_task_func_seed_consistency():
    random.seed(0)
    result1 = task_func(["Task 1", "Task 2"], 2)
    random.seed(0)
    result2 = task_func(["Task 1", "Task 2"], 2)
    assert result1.equals(result2)