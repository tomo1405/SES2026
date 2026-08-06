import matplotlib.pyplot as plt
import pandas as pd
from src_0581 import task_func


def test_task_func():
    # Test if the function returns a DataFrame
    df = task_func()
    assert isinstance(df, pd.DataFrame)

    # Test if the 'Random Numbers' column exists in the DataFrame
    assert 'Random Numbers' in df.columns

    # Test if the 'Moving Average' column exists in the DataFrame
    assert 'Moving Average' in df.columns

    # Test if the 'Random Numbers' column has the correct length
    assert len(df['Random Numbers']) == SIZE

    # Test if the 'Moving Average' column has the correct length
    assert len(df['Moving Average']) == SIZE

    # Test if the histogram plot is displayed
    assert plt.fignum_exists(1)