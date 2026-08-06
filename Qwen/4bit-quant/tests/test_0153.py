import numpy as np
import pandas as pd
from src_0153 import task_func


def test_task_func_structure():
    df = task_func()
    assert isinstance(df, pd.DataFrame), "The function should return a pandas DataFrame."
    
    # Check columns
    expected_columns = ['Name'] + COURSES + ['Average Grade']
    assert all(col in df.columns for col in expected_columns), "DataFrame does not have the correct columns."
    
    # Check number of rows
    assert len(df) == len(STUDENTS), "DataFrame does not have the correct number of rows."

def test_task_func_values():
    df = task_func()
    
    # Check each student's name is in the DataFrame
    for student in STUDENTS:
        assert student in df['Name'].values, f"Student {student} is missing from the DataFrame."
    
    # Check that each student has a grade for each course
    for index, row in df.iterrows():
        assert len(row[COURSES]) == len(COURSES), f"Student {row['Name']} does not have a grade for each course."
    
    # Check that the average grade is calculated correctly
    for index, row in df.iterrows():
        average_grade = np.mean(row[COURSES])
        assert np.isclose(row['Average Grade'], average_grade), f"Average grade for {row['Name']} is not calculated correctly."

def test_task_func_randomness():
    # Run the function multiple times to ensure randomness
    df1 = task_func()
    df2 = task_func()
    
    # Check that the dataframes are not identical
    assert not df1.equals(df2), "The DataFrames should not be identical due to randomness."