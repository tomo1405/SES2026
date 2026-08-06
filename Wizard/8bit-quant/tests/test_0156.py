python
import pandas as pd
import matplotlib.pyplot as plt

# Constants
COLUMN_NAMES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

def test_task_func():
    # Test case 1
    data = [[1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16]]
    expected_df = pd.DataFrame(data, columns=COLUMN_NAMES)
    expected_df['Average'] = expected_df.mean(axis=1)
    expected_ax = expected_df['Average'].plot()
    expected_ax.set_ylabel('Average')

    result_df, result_ax = task_func(data)

    assert expected_df.equals(result_df)
    assert expected_ax.equals(result_ax)

    # Test case 2
    data = [[1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16]]
    expected_df = pd.DataFrame(data, columns=COLUMN_NAMES)
    expected_df['Average'] = expected_df.mean(axis=1)
    expected_ax = expected_df['Average'].plot()
    expected_ax.set_ylabel('Average')

    result_df, result_ax = task_func(data)

    assert expected_df.equals(result_df)
    assert expected_ax.equals(result_ax)