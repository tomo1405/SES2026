python
import pandas as pd
import statistics
import random
import pytest

def task_func(students, subjects, seed=None):
    if seed is not None:
        random.seed(seed)

    report_data = []

    for student in students:
        grades = [random.randint(0, 100) for _ in subjects]
        avg_grade = statistics.mean(grades)
        report_data.append((student,) + tuple(grades) + (avg_grade,))

    report_df = pd.DataFrame(report_data, columns=['Student'] + subjects + ['Average Grade'])

    return report_df

def test_task_func():
    students = ['Alice', 'Bob', 'Charlie']
    subjects = ['Math', 'Science', 'English']
    seed = 42

    report_df = task_func(students, subjects, seed)

    assert report_df.shape == (3, 6)
    assert report_df.columns.tolist() == ['Student', 'Math', 'Science', 'English', 'Average Grade']
    assert report_df['Student'].tolist() == students
    assert report_df['Math'].apply(lambda x: isinstance(x, int)).all()
    assert report_df['Science'].apply(lambda x: isinstance(x, int)).all()
    assert report_df['English'].apply(lambda x: isinstance(x, int)).all()
    assert report_df['Average Grade'].apply(lambda x: isinstance(x, float)).all()