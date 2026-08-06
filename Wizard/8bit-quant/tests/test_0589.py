python
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from src_0589 import task_func

# Constants defining the range of random integers and the size of the DataFrame
RANGE = 100
SIZE = 1000

def test_task_func():
    # Generate the DataFrame with random integers within the specified range [0, RANGE)
    df = task_func()

    # Check if the DataFrame has the expected size
    assert df.shape == (SIZE, 2)

    # Check if the DataFrame has only integer values within the specified range
    assert df.X.dtype == 'int64'
    assert df.Y.dtype == 'int64'
    assert df.X.min() >= 0 and df.X.max() < RANGE
    assert df.Y.min() >= 0 and df.Y.max() < RANGE

    # Check if the scatter plot is drawn correctly
    sns.scatterplot(data=df, x='X', y='Y')
    plt.show()