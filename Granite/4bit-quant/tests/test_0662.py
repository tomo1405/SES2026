import pandas as pd
import seaborn as sns
import numpy as np
from src_0662 import task_func

# Constants
LABELS = ['H\u2082O', 'O\u2082', 'CO\u2082', 'N\u2082', 'Ar']

def test_task_func():
    x = [np.array([1, 2, 3]), np.array([4, 5, 6])]
    y = [np.array([7, 8, 9]), np.array([10, 11, 12])]
    expected_df = pd.DataFrame([
        [1, 2, 3, 7, 8, 9],
        [4, 5, 6, 10, 11, 12]
    ], index=LABELS)
    expected_ax = sns.heatmap(expected_df, cmap='coolwarm')

    ax, df = task_func(x, y, LABELS)

    assert df.equals(expected_df)
    assert ax == expected_ax