import random

import pandas as pd
from src_0309 import task_func


def test_task_func():
    # Test that the function returns a DataFrame
    assert isinstance(task_func(), pd.DataFrame)

    # Test that the DataFrame has the correct columns
    assert set(task_func().columns) == set(FIELDS + ['Average Grade'])

    # Test that the DataFrame has the correct number of rows
    assert len(task_func()) == len(STUDENTS)

    # Test that the DataFrame has the correct data types
    assert all(task_func().dtypes == object)

    # Test that the DataFrame has the correct values
    assert all(task_func()['Average Grade'] == [random.randint(0, 100) for _ in STUDENTS])

    # Test that the DataFrame has the correct index
    assert all(task_func().index == STUDENTS)

    # Test that the function returns the correct average grade for each student
    assert all(task_func()['Average Grade'] == [mean(task_func()[field]) for field in FIELDS])

    # Test that the function returns the correct average grade for each subject
    assert all(task_func().loc['Average'] == [mean(task_func()[field]) for field in FIELDS])