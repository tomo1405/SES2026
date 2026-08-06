python
import pandas as pd
import pytest
from itertools import cycle
from random import randint, seed
from src_0870 import task_func

def test_task_func():
    # Test case 1: n_grades = 0
    with pytest.raises(ValueError):
        task_func(0)

    # Test case 2: n_grades = 5, students = ['Alice', 'Bob', 'Charlie'], grade_range = range(1, 11), rng_seed = 42
    grade_df = task_func(5, ['Alice', 'Bob', 'Charlie'], range(1, 11), 42)
    assert isinstance(grade_df, pd.DataFrame)
    assert len(grade_df) == 5
    assert set(grade_df['Student']) == {'Alice', 'Bob', 'Charlie'}
    assert all(1 <= grade <= 10 for grade in grade_df['Grade'])

    # Test case 3: n_grades = 10, students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve'], grade_range = range(1, 11), rng_seed = 100
    grade_df = task_func(10, ['Alice', 'Bob', 'Charlie', 'David', 'Eve'], range(1, 11), 100)
    assert isinstance(grade_df, pd.DataFrame)
    assert len(grade_df) == 10
    assert set(grade_df['Student']) == {'Alice', 'Bob', 'Charlie', 'David', 'Eve'}
    assert all(1 <= grade <= 10 for grade in grade_df['Grade'])