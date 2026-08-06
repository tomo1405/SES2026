import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from src_0615 import task_func


def test_task_func():
    goals = {'Team A': 10, 'Team B': 5, 'Team C': 8}
    penalties = {'Team A': 3, 'Team B': 2, 'Team C': 4}

    df, plot = task_func(goals, penalties)

    # Check DataFrame
    expected_df = pd.DataFrame({
        'Team': ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'],
        'Goals': [10, 5, 8, 0, 0],
        'Penalties': [3, 2, 4, 0, 0]
    })
    pd.testing.assert_frame_equal(df, expected_df)

    # Check plot
    assert isinstance(plot, sns.axisgrid.PairGrid)
    plt.close(plot.fig)  # Close the plot to avoid memory leaks in tests