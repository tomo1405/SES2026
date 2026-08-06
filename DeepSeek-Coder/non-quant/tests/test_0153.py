import pytest
from src_0153 import task_func

def test_task_func():
    result = task_func()
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert len(result) > 0, "The DataFrame should not be empty"
    assert set(result.columns) == {'Name', 'Math', 'Physics', 'Chemistry', 'Biology', 'English', 'History', 'Geography', 'Computer Science', 'Average Grade'}
    assert all(result['Name'].isin(STUDENTS)), "All names should be in STUDENTS list"
    assert all(result['Average Grade'].between(0, 100)), "All average grades should be between 0 and 100"