import pandas as pd
import seaborn as sns
from src_0067 import task_func


def test_task_func():
    data = [
        {'col1': 'A', 'col2': 'B', 'col3': 'C'},
        {'col1': 'A', 'col2': 'B', 'col3': 'D'},
        {'col1': 'A', 'col2': 'C', 'col3': 'E'},
        {'col1': 'B', 'col2': 'C', 'col3': 'F'},
        {'col1': 'B', 'col2': 'C', 'col3': 'G'},
    ]
    expected_analyzed_df = pd.DataFrame(
        {'col1': ['A', 'B'], 'col2': ['B', 'C'], 'col3': [2, 2]},
        columns=COLUMNS
    )
    expected_ax = sns.distplot(expected_analyzed_df[COLUMNS[-1]])

    analyzed_df, ax = task_func(data)

    assert analyzed_df.equals(expected_analyzed_df)
    assert ax.equals(expected_ax)