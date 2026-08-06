python
import pandas as pd
import matplotlib.pyplot as plt
import pytest

def task_func(data_dict):
    df = pd.DataFrame(data_dict)
    axes_list = []
    for column in df.columns:
        counts = df[column].value_counts()
        uniform = (
            len(set(counts)) == 1
        )  # Check if all counts are the same (uniform distribution)

        if not uniform:
            print(f"The distribution of values in column '{column}' is not uniform.")

        ax = counts.plot(kind="bar")
        ax.set_title(column)
        axes_list.append(ax)
        plt.close()

    return axes_list

def test_task_func():
    data_dict = {
        "col1": [1, 2, 3, 4, 5],
        "col2": [1, 2, 3, 4, 5],
        "col3": [1, 2, 3, 4, 5],
    }
    axes_list = task_func(data_dict)
    assert len(axes_list) == 3
    assert isinstance(axes_list[0], plt.Axes)
    assert isinstance(axes_list[1], plt.Axes)
    assert isinstance(axes_list[2], plt.Axes)

test_task_func()