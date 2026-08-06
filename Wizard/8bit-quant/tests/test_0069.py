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
    # Test with default arguments
    df, ax = task_func()
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, sns.axisgrid.FacetGrid)

    # Test with custom arguments
    df, ax = task_func(data='/path/to/custom_data.csv', emp_prefix='CUST')
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, sns.axisgrid.FacetGrid)