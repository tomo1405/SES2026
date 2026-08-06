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
    # Mock the input dataframe
    df = pd.DataFrame({
        'Date': ['2022-01-01', '2022-01-02', '2022-01-03'],
        'Value': [10, 20, 30]
    })

    # Mock the expected output dataframe
    expected_df = pd.DataFrame({
        'Date': ['2022-01-01', '2022-01-02', '2022-01-03'],
        'Value': [10, 20, 30],
        'Value_zscore': [0.0, 1.0, 2.0]
    })

    # Mock the expected output figure
    expected_fig = plt.figure()

    # Mock the expected title, xlabel, and ylabel
    expected_title = 'Z-Scores Over Time'
    expected_xlabel = 'Date'
    expected_ylabel = 'Z-Score'

    with patch('matplotlib.pyplot.figure') as mock_figure:
        with patch.object(plt.Figure, 'add_subplot') as mock_add_subplot:
            with patch.object(plt.Axes, 'set_title') as mock_set_title:
                with patch.object(plt.Axes, 'set_xlabel') as mock_set_xlabel:
                    with patch.object(plt.Axes, 'set_ylabel') as mock_set_ylabel:
                        df_output, fig_output = task_func(df)
                        assert df_output.equals(expected_df)
                        assert fig_output == expected_fig
                        mock_figure.assert_called_once()
                        mock_add_subplot.assert_called_once_with(111)
                        mock_set_title.assert_called_once_with(expected_title)
                        mock_set_xlabel.assert_called_once_with(expected_xlabel)
                        mock_set_ylabel.assert_called_once_with(expected_ylabel)