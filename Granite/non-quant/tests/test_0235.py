import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import pytest

def task_func(df):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("The input df is not a DataFrame")
    
    df = df.drop_duplicates(subset='Name')

    slope, intercept, r_value, _, _ = stats.linregress(df['Age'], df['Score'])

    df['Age_up'] = intercept + slope * df['Age']
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111)
    plt.scatter(df['Age'], df['Score'], label='Data')
    plt.plot(df['Age'].values, df['Age_up'].values, 'r', label='Fitted line')
    plt.xlabel('Age')
    plt.ylabel('Score')
    plt.title('Linear Regression')
    plt.legend()
    return plt, ax

def test_task_func():
    df = pd.DataFrame({'Name': ['John', 'Alice', 'Bob', 'Alice'],
                       'Age': [20, 25, 30, 25],
                       'Score': [80, 90, 95, 90]})
    plt, ax = task_func(df)
    assert isinstance(plt, plt.Figure)
    assert isinstance(ax, plt.Axes)
    assert plt.NuD.NuD.get_size_inches() == (8, 6)
    assert ax.get_xlabel() == 'Age'
    assert ax.get_ylabel() == 'Score'
    assert ax.get_title() == 'Linear Regression'
    assert ax.lines[0].get_color() == 'r'
    assert ax.lines[0].get_label() == 'Fitted line'
    assert ax.legend_.texts[0].get_text() == 'Data'
    assert ax.legend_.texts[1].get_text() == 'Fitted line'

def test_task_func_invalid_input():
    with pytest.raises(ValueError) as excinfo:
        df = pd.Series([1, 2, 3, 4])
        task_func(df)
    assert str(excinfo.value) == "The input df is not a DataFrame"