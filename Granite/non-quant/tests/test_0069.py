import pandas as pd
import seaborn as sns
import pytest

def task_func(data='/path/to/data.csv', emp_prefix='EMP'):
    # Load data and filter
    df = pd.read_csv(data)
    df = df[df['Employee ID'].str.startswith(emp_prefix)]

    # Plot histogram
    ax = sns.histplot(data=df, x='Age', kde=True)

    return df, ax

def test_task_func():
    # Test case 1: Test if the function returns a tuple of length 2
    df, ax = task_func()
    assert len(df) == 2

    # Test case 2: Test if the function returns the correct data frame
    expected_columns = ['Employee ID', 'Age']
    assert all(col in df.columns for col in expected_columns)

    # Test case 3: Test if the function returns the correct histogram
    assert ax.get_xlabel() == 'Age'