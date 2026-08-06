import pandas as pd
import statistics
import random
import pytest

from src_0851 import task_func

@pytest.fixture
def students():
    return ['Alice', 'Bob', 'Charlie']

@pytest.fixture
def subjects():
    return ['Math', 'Science', 'History']

def test_task_func(students, subjects):
    report_df = task_func(students, subjects)
    assert isinstance(report_df, pd.DataFrame)
    assert report_df.shape == (len(students), len(subjects) + 2)
    assert report_df.columns.tolist() == ['Student'] + subjects + ['Average Grade']
    for student, row in report_df.iterrows():
        grades = row[subjects].tolist()
        avg_grade = row['Average Grade']
        assert isinstance(student, str)
        assert all(isinstance(grade, int) for grade in grades)
        assert 0 <= avg_grade <= 100
        assert statistics.mean(grades) == pytest.approx(avg_grade)