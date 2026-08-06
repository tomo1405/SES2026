python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pytest

def task_func(s1, s2):
    # Find the intersection data points
    intersection = set(s1).intersection(set(s2))

    # Prepare data for visualization
    df1 = pd.DataFrame({s1.name: s1, "Type": "Series1"})
    df2 = pd.DataFrame({s2.name: s2, "Type": "Series2"})
    df = pd.concat([df1, df2], axis=0, ignore_index=True)

    # Create a swarm plot
    _, ax = plt.subplots(figsize=(10, 6))
    sns.swarmplot(x=df.columns[0], y="Type", data=df, ax=ax)

    # Highlight intersection points
    for point in intersection:
        ax.axvline(x=point, color="red", linestyle="--")

    ax.set_title(f"Overlap Between {s1.name} and {s2.name}")

    return ax, len(intersection)

def test_task_func():
    s1 = pd.Series([1, 2, 3, 4, 5])
    s2 = pd.Series([4, 5, 6, 7, 8])
    ax, count = task_func(s1, s2)
    assert count == 2
    assert ax.get_title() == "Overlap Between s1 and s2"