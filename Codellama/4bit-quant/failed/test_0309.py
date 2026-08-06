import pytest
from src_0309 import task_func

def test_task_func():
    # Test that the function returns a DataFrame
    assert isinstance(task_func(), pd.DataFrame)

    # Test that the DataFrame has the correct columns
    df = task_func()
    assert set(df.columns) == set(FIELDS + ['Average Grade'])

    # Test that the DataFrame has the correct number of rows
    assert len(df) == len(STUDENTS)

    # Test that the DataFrame has the correct data types
    assert df.dtypes.to_dict() == {'Physics': int, 'Math': int, 'Chemistry': int, 'Biology': int, 'English': int, 'History': int, 'Average Grade': float}

    # Test that the function returns the correct average grade for each student
    df = task_func()
    for student in STUDENTS:
        assert df.loc[student, 'Average Grade'] == mean(df.loc[student, FIELDS])

    # Test that the function returns the correct average grade for each subject
    df = task_func()
    for field in FIELDS:
        assert df.loc['Average', field] == mean(df[field])

    # Test that the function returns the correct average grade for all subjects combined
    df = task_func()
    assert df.loc['Average', 'Average Grade'] == mean(df[FIELDS])