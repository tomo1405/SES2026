import pytest
from src_0638 import task_func
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def test_task_func_output():
    num_students = 10
    df, ax = task_func(num_students)
    
    # Check if the DataFrame has the correct shape
    assert df.shape == (num_students, 5), "DataFrame shape is incorrect"
    
    # Check if the DataFrame index contains the correct number of unique students
    assert len(df.index.unique()) == num_students, "Number of unique students is incorrect"
    
    # Check if the DataFrame columns are the correct courses
    expected_columns = ['Course1', 'Course2', 'Course3', 'Course4', 'Course5']
    assert list(df.columns) == expected_columns, "DataFrame columns are incorrect"
    
    # Check if the grades are within the expected range
    assert (df.values >= 40).all() and (df.values <= 100).all(), "Grades are out of expected range"
    
    # Check if the plot is a matplotlib Axes object
    assert isinstance(ax, plt.Axes), "Return value is not a matplotlib Axes object"

def test_task_func_with_zero_students():
    num_students = 0
    df, ax = task_func(num_students)
    
    # Check if the DataFrame is empty
    assert df.empty, "DataFrame should be empty when num_students is 0"
    
    # Check if the plot is a matplotlib Axes object
    assert isinstance(ax, plt.Axes), "Return value is not a matplotlib Axes object"

def test_task_func_with_all_students():
    num_students = 100
    df, ax = task_func(num_students)
    
    # Check if the DataFrame has the correct shape
    assert df.shape == (num_students, 5), "DataFrame shape is incorrect"
    
    # Check if the DataFrame index contains all students
    expected_index = set(['Student' + str(i) for i in range(1, 101)])
    assert set(df.index) == expected_index, "DataFrame index does not contain all students"
    
    # Check if the DataFrame columns are the correct courses
    expected_columns = ['Course1', 'Course2', 'Course3', 'Course4', 'Course5']
    assert list(df.columns) == expected_columns, "DataFrame columns are incorrect"
    
    # Check if the grades are within the expected range
    assert (df.values >= 40).all() and (df.values <= 100).all(), "Grades are out of expected range"
    
    # Check if the plot is a matplotlib Axes object
    assert isinstance(ax, plt.Axes), "Return value is not a matplotlib Axes object"