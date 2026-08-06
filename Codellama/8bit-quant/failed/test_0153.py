import pytest
from src_0153 import task_func

def test_task_func():
    grades_df = task_func()
    assert grades_df.shape == (8, 9)
    assert grades_df.columns.tolist() == ['Name', 'Math', 'Physics', 'Chemistry', 'Biology', 'English', 'History', 'Geography', 'Computer Science', 'Average Grade']
    assert grades_df['Name'].tolist() == ['Joe', 'Amy', 'Mark', 'Sara', 'John', 'Emily', 'Zoe', 'Matt']
    assert grades_df['Average Grade'].tolist() == [np.mean([randint(0, 100) for _ in COURSES]) for _ in STUDENTS]