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

    assert report_df.shape == (3, 5)
    assert report_df.columns.tolist() == ['Student', 'Math', 'Science', 'English', 'Average Grade']
    assert report_df.loc[0, 'Student'] == 'Alice'
    assert report_df.loc[1, 'Student'] == 'Bob'
    assert report_df.loc[2, 'Student'] == 'Charlie'
    assert report_df.loc[0, 'Math'] == 75
    assert report_df.loc[1, 'Math'] == 85
    assert report_df.loc[2, 'Math'] == 90
    assert report_df.loc[0, 'Science'] == 80
    assert report_df.loc[1, 'Science'] == 90
    assert report_df.loc[2, 'Science'] == 95
    assert report_df.loc[0, 'English'] == 70
    assert report_df.loc[1, 'English'] == 80
    assert report_df.loc[2, 'English'] == 85
    assert report_df.loc[0, 'Average Grade'] == 80
    assert report_df.loc[1, 'Average Grade'] == 85
    assert report_df.loc[2, 'Average Grade'] == 90