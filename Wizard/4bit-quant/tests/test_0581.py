python
import pandas as pd
import random
import statistics
import matplotlib.pyplot as plt
import numpy as np

# Constants
RANGE = 10000  # The range within which random numbers are generated
SIZE = 1000  # The number of random numbers to generate
BIN_WIDTH = 100  # The width of bins for the histogram

def task_func():
    numbers = [random.randint(0, RANGE) for _ in range(SIZE)]
    moving_avg = [statistics.mean(numbers[max(0, i - 5):i + 1]) for i in range(SIZE)]

    df = pd.DataFrame({
        'Random Numbers': numbers,
        'Moving Average': moving_avg
    })

    plt.hist(df['Random Numbers'],
             bins=np.arange(min(df['Random Numbers']), max(df['Random Numbers']) + BIN_WIDTH, BIN_WIDTH))
    plt.title('Histogram of Random Numbers')
    plt.xlabel('Random Numbers')
    plt.ylabel('Frequency')
    plt.show()

    return df

def test_task_func():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == SIZE
    assert df.columns.tolist() == ['Random Numbers', 'Moving Average']
    assert df['Random Numbers'].max() <= RANGE
    assert df['Random Numbers'].min() >= 0
    assert df['Moving Average'].max() <= RANGE
    assert df['Moving Average'].min() >= 0
    assert df['Moving Average'].mean() <= RANGE
    assert df['Moving Average'].mean() >= 0
    assert df['Moving Average'].std() <= RANGE
    assert df['Moving Average'].std() >= 0
    assert df['Moving Average'].median() <= RANGE
    assert df['Moving Average'].median() >= 0
    assert df['Moving Average'].quantile(0.25) <= RANGE
    assert df['Moving Average'].quantile(0.25) >= 0
    assert df['Moving Average'].quantile(0.75) <= RANGE
    assert df['Moving Average'].quantile(0.75) >= 0
    assert df['Moving Average'].describe()['count'] == SIZE
    assert df['Moving Average'].describe()['mean'] <= RANGE
    assert df['Moving Average'].describe()['mean'] >= 0
    assert df['Moving Average'].describe()['std'] <= RANGE
    assert df['Moving Average'].describe()['std'] >= 0
    assert df['Moving Average'].describe()['min'] <= RANGE
    assert df['Moving Average'].describe()['min'] >= 0
    assert df['Moving Average'].describe()['25%'] <= RANGE
    assert df['Moving Average'].describe()['25%'] >= 0
    assert df['Moving Average'].describe()['50%'] <= RANGE
    assert df['Moving Average'].describe()['50%'] >= 0
    assert df['Moving Average'].describe()['75%'] <= RANGE
    assert df['Moving Average'].describe()['75%'] >= 0
    assert df['Moving Average'].describe()['max'] <= RANGE
    assert df['Moving Average'].describe()['max'] >= 0
    assert df['Moving Average'].hist(bins=np.arange(min(df['Random Numbers']), max(df['Random Numbers']) + BIN_WIDTH, BIN_WIDTH))