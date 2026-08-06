import pytest
from src_0851 import task_func

def test_task_func():
    students = ['Alice', 'Bob', 'Charlie']
    subjects = ['Math', 'English', 'Science']
    seed = 1234

    report_df = task_func(students, subjects, seed)

    assert report_df.columns.tolist() == ['Student', 'Math', 'English', 'Science', 'Average Grade']
    assert report_df.shape == (3, 5)
    assert report_df.loc['Alice', 'Math'] >= 0 and report_df.loc['Alice', 'Math'] <= 100
    assert report_df.loc['Alice', 'English'] >= 0 and report_df.loc['Alice', 'English'] <= 100
    assert report_df.loc['Alice', 'Science'] >= 0 and report_df.loc['Alice', 'Science'] <= 100
    assert report_df.loc['Alice', 'Average Grade'] >= 0 and report_df.loc['Alice', 'Average Grade'] <= 100
    assert report_df.loc['Bob', 'Math'] >= 0 and report_df.loc['Bob', 'Math'] <= 100
    assert report_df.loc['Bob', 'English'] >= 0 and report_df.loc['Bob', 'English'] <= 100
    assert report_df.loc['Bob', 'Science'] >= 0 and report_df.loc['Bob', 'Science'] <= 100
    assert report_df.loc['Bob', 'Average Grade'] >= 0 and report_df.loc['Bob', 'Average Grade'] <= 100
    assert report_df.loc['Charlie', 'Math'] >= 0 and report_df.loc['Charlie', 'Math'] <= 100
    assert report_df.loc['Charlie', 'English'] >= 0 and report_df.loc['Charlie', 'English'] <= 100
    assert report_df.loc['Charlie', 'Science'] >= 0 and report_df.loc['Charlie', 'Science'] <= 100
    assert report_df.loc['Charlie', 'Average Grade'] >= 0 and report_df.loc['Charlie', 'Average Grade'] <= 100