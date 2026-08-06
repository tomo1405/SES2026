import pandas as pd
from statistics import mean
import random
import pytest
from src_0309 import task_func

FIELDS = ['Physics', 'Math', 'Chemistry', 'Biology', 'English', 'History']
STUDENTS = ['Student_' + str(i) for i in range(1, 101)]

def test_task_func():
    # Test with no additional fields
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert df.index.tolist() == STUDENTS
    assert df.columns.tolist() == FIELDS + ['Average Grade']
    for field in FIELDS:
        assert df[field].tolist() == [random.randint(0, 100) for _ in STUDENTS]
    assert df['Average Grade'].tolist() == [mean(df[field]) for field in FIELDS]

    # Test with additional fields
    additional_fields = ['Geography', 'Computer Science']
    df = task_func(additional_fields)
    assert df.columns.tolist() == FIELDS + additional_fields + ['Average Grade']

if __name__ == '__main__':
    pytest.main()