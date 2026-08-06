python
import pandas as pd
import pytest
from itertools import cycle
from random import randint, seed
from src_0870 import task_func

def test_task_func():
    # Test case 1: n_grades = 0
    grade_df = task_func(0)
    assert grade_df.empty

    # Test case 2: n_grades = 1, students = ['Alice'], grade_range = range(1, 11), rng_seed = 123
    grade_df = task_func(1, ['Alice'], range(1, 11), 123)
    assert grade_df.shape == (1, 2)
    assert grade_df.iloc[0]['Student'] == 'Alice'
    assert grade_df.iloc[0]['Grade'] in range(1, 11)

    # Test case 3: n_grades = 5, students = ['Alice', 'Bob', 'Charlie'], grade_range = range(1, 11), rng_seed = 456
    grade_df = task_func(5, ['Alice', 'Bob', 'Charlie'], range(1, 11), 456)
    assert grade_df.shape == (5, 2)
    assert grade_df['Student'].isin(['Alice', 'Bob', 'Charlie']).all()
    assert grade_df['Grade'].apply(lambda x: x in range(1, 11)).all()

    # Test case 4: n_grades = 10, students = [], grade_range = range(1, 11), rng_seed = 789
    with pytest.raises(ValueError):
        grade_df = task_func(10, [], range(1, 11), 789)

    # Test case 5: n_grades = 10, students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve'], grade_range = range(1, 11), rng_seed = 101112
    grade_df = task_func(10, ['Alice', 'Bob', 'Charlie', 'David', 'Eve'], range(1, 11), 101112)
    assert grade_df.shape == (10, 2)
    assert grade_df['Student'].isin(['Alice', 'Bob', 'Charlie', 'David', 'Eve']).all()
    assert grade_df['Grade'].apply(lambda x: x in range(1, 11)).all()