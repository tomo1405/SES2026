python
import pandas as pd
import pytest
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Constants
COLUMNS = ['Date', 'Value']

def task_func(df, plot=False):
    df['Date'] = pd.to_datetime(df['Date'])
    df = pd.concat([df['Date'], df['Value'].apply(pd.Series)], axis=1)
    
    scaler = StandardScaler()
    df.iloc[:,1:] = scaler.fit_transform(df.iloc[:,1:])
    
    if plot:
        plt.figure()
        ax = df.set_index('Date').plot(kind='bar', stacked=True)
        plt.title('Scaled Values Over Time')
        plt.xlabel('Date')
        plt.ylabel('Scaled Value')
        return df, ax

    return df

# Test 1
def test_task_func_valid_input():
    df = pd.DataFrame({'Date': ['2021-01-01', '2021-01-02', '2021-01-03'], 'Value': [1, 2, 3]})
    result = task_func(df)
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (3, 2)
    assert result.columns.tolist() == ['Date', 'Value']
    assert result['Date'].dtype == 'datetime64[ns]'
    assert result['Value'].dtype == 'float64'

# Test 2
def test_task_func_invalid_input():
    df = pd.DataFrame({'Date': ['2021-01-01', '2021-01-02', '2021-01-03'], 'Value': ['a', 'b', 'c']})
    with pytest.raises(ValueError):
        task_func(df)

# Test 3
def test_task_func_plot():
    df = pd.DataFrame({'Date': ['2021-01-01', '2021-01-02', '2021-01-03'], 'Value': [1, 2, 3]})
    result, ax = task_func(df, plot=True)
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (3, 2)
    assert result.columns.tolist() == ['Date', 'Value']
    assert result['Date'].dtype == 'datetime64[ns]'
    assert result['Value'].dtype == 'float64'
    assert isinstance(ax, plt.Axes)