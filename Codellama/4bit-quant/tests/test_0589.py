import pandas as pd
from src_0589 import task_func


def test_task_func():
    # Test that the function returns a DataFrame with the correct shape
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (SIZE, 2)

    # Test that the DataFrame contains only integers within the specified range
    assert np.all(df['X'] >= 0)
    assert np.all(df['X'] < RANGE)
    assert np.all(df['Y'] >= 0)
    assert np.all(df['Y'] < RANGE)

    # Test that the scatter plot is drawn correctly
    assert plt.gcf().axes[0].get_xlabel() == 'X'
    assert plt.gcf().axes[0].get_ylabel() == 'Y'
    assert plt.gcf().axes[0].get_title() == 'Scatter Plot'