python
import pandas as pd
import pytest
from itertools import cycle
from random import randint, seed
from src_0870 import task_func

def test_task_func():
    # Test case 1: n_grades = 5, students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve'], grade_range = range(1, 11), rng_seed = None
    n_grades = 5
    students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
    grade_range = range(1, 11)
    rng_seed = None
    expected_result = pd.DataFrame(
        data=[
            ['Alice', 7],
            ['Bob', 10],
            ['Charlie', 1],
            ['David', 10],
            ['Eve', 10]
        ],
        columns=['Student', 'Grade']
    )
    result = task_func(n_grades, students, grade_range, rng_seed)
    assert result.equals(expected_result)

    # Test case 2: n_grades = 0, students = [], grade_range = range(1, 11), rng_seed = None
    n_grades = 0
    students = []
    grade_range = range(1, 11)
    rng_seed = None
    with pytest.raises(ValueError):
        task_func(n_grades, students, grade_range, rng_seed)

    # Test case 3: n_grades = 5, students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve'], grade_range = range(1, 11), rng_seed = 123
    n_grades = 5
    students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
    grade_range = range(1, 11)
    rng_seed = 123
    expected_result = pd.DataFrame(
        data=[
            ['Alice', 10],
            ['Bob', 1],
            ['Charlie', 10],
            ['David', 1],
            ['Eve', 7]
        ],
        columns=['Student', 'Grade']
    )
    result = task_func(n_grades, students, grade_range, rng_seed)
    assert result.equals(expected_result)