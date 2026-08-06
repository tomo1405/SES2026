import pytest
from src_0851 import task_func
import pandas as pd

def test_task_func_with_seed():
    students = ['Alice', 'Bob']
    subjects = ['Math', 'Science']
    seed = 42
    expected_output = pd.DataFrame({
        'Student': ['Alice', 'Bob'],
        'Math': [71, 60],
        'Science': [91, 85],
        'Average Grade': [81.0, 72.5]
    })
    
    result_df = task_func(students, subjects, seed=seed)
    pd.testing.assert_frame_equal(result_df, expected_output)

def test_task_func_without_seed():
    students = ['Charlie', 'David']
    subjects = ['History', 'Geography']
    
    result_df = task_func(students, subjects)
    assert isinstance(result_df, pd.DataFrame)
    assert len(result_df) == len(students)
    assert all(subject in result_df.columns for subject in subjects)
    assert 'Average Grade' in result_df.columns

def test_task_func_single_student():
    students = ['Eve']
    subjects = ['Art', 'Music']
    seed = 123
    expected_output = pd.DataFrame({
        'Student': ['Eve'],
        'Art': [45],
        'Music': [67],
        'Average Grade': [56.0]
    })
    
    result_df = task_func(students, subjects, seed=seed)
    pd.testing.assert_frame_equal(result_df, expected_output)

def test_task_func_no_subjects():
    students = ['Frank']
    subjects = []
    seed = 321
    expected_output = pd.DataFrame({
        'Student': ['Frank'],
        'Average Grade': [0.0]
    })
    
    result_df = task_func(students, subjects, seed=seed)
    pd.testing.assert_frame_equal(result_df, expected_output)