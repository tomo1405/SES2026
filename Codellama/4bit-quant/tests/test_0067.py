import pandas as pd
from src_0067 import task_func


def test_task_func():
    data = [
        {'col1': 'A', 'col2': 'B', 'col3': 'C'},
        {'col1': 'A', 'col2': 'B', 'col3': 'D'},
        {'col1': 'A', 'col2': 'B', 'col3': 'E'},
        {'col1': 'A', 'col2': 'B', 'col3': 'F'},
        {'col1': 'A', 'col2': 'B', 'col3': 'G'},
        {'col1': 'A', 'col2': 'B', 'col3': 'H'},
        {'col1': 'A', 'col2': 'B', 'col3': 'I'},
        {'col1': 'A', 'col2': 'B', 'col3': 'J'},
        {'col1': 'A', 'col2': 'B', 'col3': 'K'},
        {'col1': 'A', 'col2': 'B', 'col3': 'L'},
        {'col1': 'A', 'col2': 'B', 'col3': 'M'},
        {'col1': 'A', 'col2': 'B', 'col3': 'N'},
        {'col1': 'A', 'col2': 'B', 'col3': 'O'},
        {'col1': 'A', 'col2': 'B', 'col3': 'P'},
        {'col1': 'A', 'col2': 'B', 'col3': 'Q'},
        {'col1': 'A', 'col2': 'B', 'col3': 'R'},
        {'col1': 'A', 'col2': 'B', 'col3': 'S'},
        {'col1': 'A', 'col2': 'B', 'col3': 'T'},
        {'col1': 'A', 'col2': 'B', 'col3': 'U'},
        {'col1': 'A', 'col2': 'B', 'col3': 'V'},
        {'col1': 'A', 'col2': 'B', 'col3': 'W'},
        {'col1': 'A', 'col2': 'B', 'col3': 'X'},
        {'col1': 'A', 'col2': 'B', 'col3': 'Y'},
        {'col1': 'A', 'col2': 'B', 'col3': 'Z'}
    ]
    expected_analyzed_df = pd.DataFrame(
        {'col1': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
         'col2': ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
         'col3': ['C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        })
    expected_ax = sns.distplot(expected_analyzed_df['col3'])

    analyzed_df, ax = task_func(data)

    assert analyzed_df.equals(expected_analyzed_df)
    assert ax.equals(expected_ax)