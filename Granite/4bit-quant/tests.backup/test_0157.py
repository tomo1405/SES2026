import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import pytest

def task_func(data):
    COLUMN_NAMES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    scaler = MinMaxScaler()
    normalized_data = scaler.fit_transform(data)

    df = pd.DataFrame(normalized_data, columns=COLUMN_NAMES)
    df['Average'] = df.mean(axis=1)

    fig, ax = plt.subplots()
    df['Average'].plot(ax=ax)

    return df, ax

def test_task_func():
    # Test case 1: Test with a dataset of size 10x8
    data = [[1, 2, 3, 4, 5, 6, 7, 8],
            [9, 8, 7, 6, 5, 4, 3, 2],
            [3, 4, 5, 6, 7, 8, 9, 0],
            [0, 1, 2, 3, 4, 5, 6, 7],
            [8, 7, 6, 5, 4, 3, 2, 1],
            [2, 3, 4, 5, 6, 7, 8, 9],
            [9, 0, 1, 2, 3, 4, 5, 6],
            [7, 6, 5, 4, 3, 2, 1, 0],
            [1, 2, 3, 4, 5, 6, 7, 8],
            [9, 8, 7, 6, 5, 4, 3, 2]]
    expected_df_shape = (10, 9)
    expected_ax_label = 'Average'

    df, ax = task_func(data)

    assert df.shape == expected_df_shape
    assert ax.get_ylabel() == expected_ax_label

    # Test case 2: Test with a dataset of size 5x4
    data = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 0, 1, 2],
            [3, 4, 5, 6],
            [7, 8, 9, 0]]
    expected_df_shape = (5, 5)
    expected_ax_label = 'Average'

    df, ax = task_func(data)

    assert df.shape == expected_df_shape
    assert ax.get_ylabel() == expected_ax_label

if __name__ == "__main__":
    pytest.main()