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
    assert report_df['Math'].tolist() == [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]
    assert report_df['English'].tolist() == [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]
    assert report_df['Science'].tolist() == [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]
    assert report_df['Average Grade'].tolist() == [statistics.mean([random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]),
                                                statistics.mean([random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]),
                                                statistics.mean([random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)])]