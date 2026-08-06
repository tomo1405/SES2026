python
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
    # Test case 1: Valid input
    df, ax = task_func(data='data.csv', emp_prefix='EMP')
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, sns.axisgrid.FacetGrid)

    # Test case 2: Invalid input
    with pytest.raises(FileNotFoundError):
        task_func(data='invalid_file.csv', emp_prefix='EMP')

    # Test case 3: Empty input
    with pytest.raises(ValueError):
        task_func(data='', emp_prefix='EMP')

    # Test case 4: Invalid prefix
    with pytest.raises(ValueError):
        task_func(data='data.csv', emp_prefix='INVALID')