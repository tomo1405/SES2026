import matplotlib.pyplot as plt
import pandas as pd
from src_0532 import task_func


def test_task_func():
    # Mock input data
    df = pd.DataFrame({
        "x": [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
        "y": [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    })

    # Call the function with mock data
    duplicates_counter, unique_df, ax = task_func(df)

    # Perform assertions on the output
    assert isinstance(duplicates_counter, dict)
    assert isinstance(unique_df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert len(unique_df) == len(df) - len(duplicates_counter)
    assert ax.get_xlabel() == "x"
    assert ax.get_ylabel() == "y"
    assert ax.get_title() == "KMeans Clusters"