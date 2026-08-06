import random

import pandas as pd
import pytest
from src_0953 import task_func


@pytest.fixture
def task_list():
    return ["Task 1", "Task 2", "Task 3"]

def test_task_func_with_valid_input(task_list):
    assignment_df = task_func(task_list=task_list, n_tasks=2)
    assert isinstance(assignment_df, pd.DataFrame)
    assert assignment_df.shape == (2, 3)
    assert assignment_df.columns.tolist() == ["Task Name", "Assigned To", "Due Date"]

def test_task_func_with_invalid_input():
    with pytest.raises(ValueError):
        task_func(task_list=[], n_tasks=-1)

def test_task_func_with_seed(task_list):
    seed = 42
    random.seed(seed)
    assignment_df_1 = task_func(task_list=task_list, n_tasks=2, seed=seed)
    random.seed(seed)
    assignment_df_2 = task_func(task_list=task_list, n_tasks=2, seed=seed)
    assert assignment_df_1.equals(assignment_df_2)