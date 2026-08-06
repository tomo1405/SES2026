import pytest
from src_0851 import task_func

def test_task_func():
    students = ['Alice', 'Bob', 'Charlie']
    subjects = ['Math', 'English', 'Science']
    seed = 1234

    report_df = task_func(students, subjects, seed)

    assert report_df.shape == (3, 5)
    assert report_df.columns.tolist() == ['Student', 'Math', 'English', 'Science', 'Average Grade']
    assert report_df['Student'].tolist() == ['Alice', 'Bob', 'Charlie']
    assert report_df['Math'].tolist() == [75, 85, 90]
    assert report_df['English'].tolist() == [80, 70, 95]
    assert report_df['Science'].tolist() == [90, 85, 80]
    assert report_df['Average Grade'].tolist() == [82.5, 80, 85]