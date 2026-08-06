python
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from src_0589 import task_func

def test_task_func():
    # Generate the DataFrame with random integers within the specified range [0, RANGE)
    df = pd.DataFrame({
        'X': np.random.randint(0, 100, 1000),
        'Y': np.random.randint(0, 100, 1000)
    })

    # Draw a scatter plot using Seaborn for a more refined visual output
    sns.scatterplot(data=df, x='X', y='Y')
    plt.show()

    # Check if the function returns the expected DataFrame
    assert df.equals(task_func())