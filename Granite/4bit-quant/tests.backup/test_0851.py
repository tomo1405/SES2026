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
    subjects = ['Math', 'Science', 'History']
    seed = 42
    report_df = task_func(students, subjects, seed)
    assert report_df.shape == (3, 6)
    assert report_df.columns.tolist() == ['Student', 'Math', 'Science', 'History', 'Average Grade']
    expected_grades = [[75, 80, 85, 85], [65, 70, 75, 75], [85, 90, 95, 95]]
    for i, row in report_df.iterrows():
        assert row['Student'] in students
        assert row['Average Grade'] == statistics.mean(expected_grades[i])

if __name__ == '__main__':
    pytest.main()