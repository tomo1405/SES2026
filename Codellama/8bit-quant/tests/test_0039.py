import matplotlib.pyplot as plt
import pandas as pd
from src_0039 import task_func


def test_task_func():
    data_matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
    expected_df = pd.DataFrame(
        [[-1.0, -1.0, -1.0, -1.0, -1.0], [1.0, 1.0, 1.0, 1.0, 1.0]],
        columns=FEATURE_NAMES,
    )
    expected_ax = plt.figure(figsize=(10, 5)).axes[0]
    expected_ax.set_title("Distribution of Means")
    expected_ax.set_xlabel("Mean")
    expected_ax.set_ylabel("Count")
    expected_ax.set_xlim([-1.0, 1.0])
    expected_ax.set_ylim([0, 2])

    df, ax = task_func(data_matrix)

    assert df.equals(expected_df)
    assert ax.get_title() == expected_ax.get_title()
    assert ax.get_xlabel() == expected_ax.get_xlabel()
    assert ax.get_ylabel() == expected_ax.get_ylabel()
    assert ax.get_xlim() == expected_ax.get_xlim()
    assert ax.get_ylim() == expected_ax.get_ylim()