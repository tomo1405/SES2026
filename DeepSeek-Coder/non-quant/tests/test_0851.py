import pytest
from src_0851 import task_func
import pandas as pd
import random
import statistics

@pytest.fixture
def setup():
    students = ['Alice', 'Bob', 'Charlie']
    subjects = ['Math', 'Science', 'History']
    seed = 42
    return students, subjects, seed

def test_task_func(setup):
    students, subjects, seed = setup
    result = task_func(students=students, subjects=subjects, seed=seed)
    
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert len(result) == len(students), "The number of rows should be equal to the number of students"
    assert len(result.columns) == len(subjects) + 2, "The number of columns should be the number of subjects plus the average grade column"
    assert 'Average Grade' in result.columns, "The DataFrame should contain an 'Average Grade' column"

    # Additional assertions to check the correctness of the data
    for student in students:
        row = result[result['Student'] == student]
        assert len(row) == 1, f"Expected exactly one row for student {student}"
        grades = row.iloc[0][1:-1]  # Exclude the student name and average grade
        assert all(0 <= grade <= 100 for grade in grades), "All grades should be between 0 and 100"
        assert 0 <= row.iloc[0]['Average Grade'] <= 100, "The average grade should be between 0 and 100"