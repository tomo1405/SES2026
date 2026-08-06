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
    # Test case 1: Test if the function returns a DataFrame and an Axes object
    df, ax = task_func(data='path/to/data.csv', emp_prefix='EMP')
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, sns.axisgrid.Axes)

    # Test case 2: Test if the function returns the expected DataFrame and Axes object
    expected_df = pd.read_csv('path/to/data.csv')
    expected_df = expected_df[expected_df['Employee ID'].str.startswith('EMP')]
    expected_ax = sns.histplot(data=expected_df, x='Age', kde=True)
    assert df.equals(expected_df)
    assert ax == expected_ax

    # Test case 3: Test if the function raises an exception when the input file does not exist
    with pytest.raises(FileNotFoundError):
        task_func(data='path/to/nonexistent.csv', emp_prefix='EMP')