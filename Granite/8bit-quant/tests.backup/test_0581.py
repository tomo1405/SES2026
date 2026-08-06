import pandas as pd
import random
import statistics
import matplotlib.pyplot as plt
import numpy as np
from src_0581 import task_func

def test_task_func():
    # Test that the function returns a DataFrame
    df = task_func()
    assert isinstance(df, pd.DataFrame)

    # Test that the 'Random Numbers' column exists in the DataFrame
    assert 'Random Numbers' in df.columns

    # Test that the 'Moving Average' column exists in the DataFrame
    assert 'Moving Average' in df.columns

    # Test that the histogram was created
    assert plt.fignum_exists(0)