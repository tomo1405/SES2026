import pandas as pd
from scipy.stats import zscore
import matplotlib.pyplot as plt
from unittest.mock import patch

def task_func(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df = pd.concat([df['Date'], df['Value'].apply(pd.Series)], axis=1)
    df.iloc[:,1:] = df.iloc[:,1:].apply(zscore)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    df.set_index('Date').boxplot(ax=ax)
    ax.set_title('Z-Scores Over Time')
    ax.set_xlabel('Date')
    ax.set_ylabel('Z-Score')
    return df, fig

def test_task_func():
    # Mock the input data
    df = pd.DataFrame({
        'Date': ['2022-01-01', '2022-01-02', '2022-01-03'],
        'Value': [10, 20, 30]
    })

    # Mock the expected output data
    expected_df = pd.DataFrame({
        'Date': ['2022-01-01', '2022-01-02', '2022-01-03'],
        'Value': [10, 20, 30],
        'Value_zscore': [0.0, 1.22474487, 2.44948974]
    })
    expected_fig = plt.figure()
    ax = expected_fig.add_subplot(111)
    expected_df.set_index('Date').boxplot(ax=ax)
    ax.set_title('Z-Scores Over Time')
    ax.set_xlabel('Date')
    ax.set_ylabel('Z-Score')

    # Call the function and compare the output with the expected output
    with patch('matplotlib.pyplot.show') as mock_show:
        df, fig = task_func(df)
        assert df.equals(expected_df)
        assert fig == expected_fig
        mock_show.assert_called_once()

test_task_func()