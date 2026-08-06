import pandas as pd
import pytest
from src_0870 import task_func


def test_task_func_valid_input():
    n_grades = 10
    students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
    grade_range = range(1, 11)
    rng_seed = None

    grade_df = task_func(n_grades, students, grade_range, rng_seed)

    assert isinstance(grade_df, pd.DataFrame)
    assert grade_df.shape == (n_grades, 2)
    assert grade_df.columns.tolist() == ['Student', 'Grade']
    assert all(grade_df['Student'].isin(students))
    assert all(grade_df['Grade'].isin(grade_range))

def test_task_func_invalid_input():
    n_grades = 10
    students = []
    grade_range = range(1, 11)
    rng_seed = None

    with pytest.raises(ValueError):
        task_func(n_grades, students, grade_range, rng_seed)