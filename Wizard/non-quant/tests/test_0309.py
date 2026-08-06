python
import pandas as pd
import pytest
from src_0309 import task_func

FIELDS = ['Physics', 'Math', 'Chemistry', 'Biology', 'English', 'History']
STUDENTS = ['Student_' + str(i) for i in range(1, 101)]

def test_task_func():
    # Test with default fields
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == FIELDS + ['Average Grade']
    assert list(df.index) == STUDENTS + ['Average']
    assert df.shape == (101, 7)
    assert df.loc['Average', 'Math'] == df['Math'].mean()
    assert df.loc['Average', 'Biology'] == df['Biology'].mean()
    assert df.loc['Average', 'Average Grade'] == df['Average Grade'].mean()

    # Test with additional fields
    additional_fields = ['Science', 'Geography']
    df = task_func(additional_fields)
    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == FIELDS + additional_fields + ['Average Grade']
    assert list(df.index) == STUDENTS + ['Average']
    assert df.shape == (101, 9)
    assert df.loc['Average', 'Math'] == df['Math'].mean()
    assert df.loc['Average', 'Biology'] == df['Biology'].mean()
    assert df.loc['Average', 'Science'] == df['Science'].mean()
    assert df.loc['Average', 'Geography'] == df['Geography'].mean()
    assert df.loc['Average', 'Average Grade'] == df['Average Grade'].mean()