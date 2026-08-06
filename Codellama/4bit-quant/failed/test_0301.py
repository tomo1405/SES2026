import pytest
from src_0301 import task_func
import pandas as pd
from scipy.stats import zscore
import matplotlib.pyplot as plt

def test_task_func():
    df = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'],
                   'Value': [10, 20, 30]})
    df['Date'] = pd.to_datetime(df['Date'])
    df = pd.concat([df['Date'], df['Value'].apply(pd.Series)], axis=1)
    df.iloc[:,1:] = df.iloc[:,1:].apply(zscore)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    df.set_index('Date').boxplot(ax=ax)
    ax.set_title('Z-Scores Over Time')
    ax.set_xlabel('Date')
    ax.set_ylabel('Z-Score')
    assert df.equals(pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'],
                                  'Value': [10, 20, 30],
                                  'Value_zscore': [0, 0, 0]})
    assert fig.axes[0].get_title() == 'Z-Scores Over Time'
    assert fig.axes[0].get_xlabel() == 'Date'
    assert fig.axes[0].get_ylabel() == 'Z-Score'
    assert len(fig.axes[0].get_xticks()) == 3
    assert len(fig.axes[0].get_yticks()) == 3
    assert fig.axes[0].get_xticks()[0] == '2022-01-01'
    assert fig.axes[0].get_xticks()[1] == '2022-01-02'
    assert fig.axes[0].get_xticks()[2] == '2022-01-03'
    assert fig.axes[0].get_yticks()[0] == 0
    assert fig.axes[0].get_yticks()[1] == 0
    assert fig.axes[0].get_yticks()[2] == 0