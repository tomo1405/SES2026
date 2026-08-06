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

    # Check if the DataFrame contains only integers within the specified range
    assert df.X.between(0, RANGE-1).all()
    assert df.Y.between(0, RANGE-1).all()

    # Check if the scatter plot is drawn correctly
    sns.scatterplot(data=df, x='X', y='Y')
    plt.show()