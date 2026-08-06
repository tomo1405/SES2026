import pytest
from src_0638 import task_func
import numpy as np
import pandas as pd

def test_task_func_output():
    num_students = 10
    df, ax = task_func(num_students)
    
    # Check if the DataFrame has the correct shape
    assert df.shape == (num_students, 5), "DataFrame shape is incorrect"
    
    # Check if the DataFrame contains only 'Student' and 'Course' labels
    assert all(df.index.str.startswith('Student')), "Index does not contain 'Student' labels"
    assert all(df.columns.str.startswith('Course')), "Columns do not contain 'Course' labels"
    
    # Check if the grades are within the expected range
    assert df.values.min() >= 40, "Minimum grade is less than 40"
    assert df.values.max() <= 100, "Maximum grade is greater than 100"
    
    # Check if the plot object is created
    assert isinstance(ax, plt.Axes), "Plot object is not of type plt.Axes"

def test_task_func_edge_cases():
    # Test with minimum number of students
    df_min, _ = task_func(1)
    assert df_min.shape == (1, 5), "DataFrame shape is incorrect for minimum students"
    
    # Test with maximum number of students
    df_max, _ = task_func(100)
    assert df_max.shape == (100, 5), "DataFrame shape is incorrect for maximum students"
    
    # Test with zero students (should raise an error or handle gracefully)
    with pytest.raises(ValueError):
        task_func(0)

def test_task_func_data_types():
    num_students = 10
    df, _ = task_func(num_students)
    
    # Check if the DataFrame is of type pandas.DataFrame
    assert isinstance(df, pd.DataFrame), "Return value is not a pandas DataFrame"
    
    # Check if the plot object is of type matplotlib.axes._subplots.AxesSubplot
    assert isinstance(ax, plt.Axes), "Plot object is not of type plt.Axes"