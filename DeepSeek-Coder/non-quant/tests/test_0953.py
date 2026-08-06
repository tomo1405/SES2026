import pytest
from src_0953 import task_func

# Test cases for task_func

def test_task_func_basic():
    task_list = ["Task 1", "Task 2", "Task 3"]
    n_tasks = 3
    result = task_func(task_list=task_list, n_tasks=n_tasks)
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert len(result) == n_tasks, "The number of tasks assigned should match n_tasks"

def test_task_func_with_seed():
    task_list = ["Task 1", "Task 2", "Task 3"]
    n_tasks = 3
    seed = 42
    result = task_func(task_list=task_list, n_tasks=n_tasks, seed=seed)
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert len(result) == n_tasks, "The number of tasks assigned should match n_tasks"

def test_task_func_negative_n_tasks():
    task_list = ["Task 1", "Task 2", "Task 3"]
    n_tasks = -1
    with pytest.raises(ValueError):
        task_func(task_list=task_list, n_tasks=n_tasks)

def test_task_func_empty_task_list():
    task_list = []
    n_tasks = 3
    result = task_func(task_list=task_list, n_tasks=n_tasks)
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert len(result) == 0, "The DataFrame should be empty"