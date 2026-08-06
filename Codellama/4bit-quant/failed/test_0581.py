import pytest
from src_0581 import task_func

def test_task_func():
    # Test that the function returns a pandas DataFrame
    assert isinstance(task_func(), pd.DataFrame)

    # Test that the DataFrame has the correct columns
    df = task_func()
    assert 'Random Numbers' in df.columns
    assert 'Moving Average' in df.columns

    # Test that the DataFrame has the correct number of rows
    assert len(df) == SIZE

    # Test that the histogram is created correctly
    assert plt.hist(df['Random Numbers'],
                    bins=np.arange(min(df['Random Numbers']), max(df['Random Numbers']) + BIN_WIDTH, BIN_WIDTH))
    assert plt.title('Histogram of Random Numbers')
    assert plt.xlabel('Random Numbers')
    assert plt.ylabel('Frequency')
    assert plt.show()