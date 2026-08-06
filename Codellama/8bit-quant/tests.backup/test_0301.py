import pytest
from src_0301 import task_func
import pandas as pd
from scipy.stats import zscore
import matplotlib.pyplot as plt

def test_task_func():
    df = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'],
                      'Value': [10, 20, 30]})
    df_expected = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'],
                              'Value': [10, 20, 30]})
    df_expected.iloc[:,1:] = df_expected.iloc[:,1:].apply(zscore)
    fig_expected = plt.figure()
    ax_expected = fig_expected.add_subplot(111)
    df_expected.set_index('Date').boxplot(ax=ax_expected)
    ax_expected.set_title('Z-Scores Over Time')
    ax_expected.set_xlabel('Date')
    ax_expected.set_ylabel('Z-Score')
    
    df_actual, fig_actual = task_func(df)
    
    assert df_actual.equals(df_expected)
    assert fig_actual.equals(fig_expected)